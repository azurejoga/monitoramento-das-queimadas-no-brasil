# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a20f6c0d-cc68-3c8f-a1c2-74b13f7bc7fb | -10.4794 | -64.5012 | 2026-08-29 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| bdfd4b66-cd65-36a6-964d-c19bf87b6e28 | -7.5137 | -55.3051 | 2026-08-29 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f7074648-2e6e-3b9f-801d-fa73cf8a34b8 | -6.7884 | -55.6635 | 2026-08-29 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| efeae498-f6a4-3312-841a-b932fc60250e | -6.6315 | -43.7533 | 2026-08-29 05:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e1c3575e-7d1b-3803-89b3-1b882730623b | -5.8895 | -57.7513 | 2026-08-29 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| e481f6e2-20c2-3e8d-bb7f-e87fdf9e6306 | -6.7699 | -55.6644 | 2026-08-29 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| e055f7db-c6d9-3a25-949a-6c0aa3692220 | 3.23595 | -60.13795 | 2026-08-29 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df4a8759-b6cb-3ca2-a06f-1aa354779c50 | 2.5178 | -50.85502 | 2026-08-29 05:33:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72a7a3d1-9f06-3f37-86a6-6659e3dd43e3 | 0.91221 | -59.62653 | 2026-08-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4fa6b2fe-4fb2-33fc-85a8-3e98cbbb08c3 | 0.61548 | -60.15494 | 2026-08-29 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5621471e-9a00-3c97-8caf-b1205f3c133e | 2.40746 | -60.88059 | 2026-08-29 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd14deac-c48b-3e47-8bd0-4bc81102eceb | 0.14538 | -60.40138 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa0bdedf-b2fe-3c96-b600-b4ebfda20555 | 1.1634 | -60.67081 | 2026-08-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1c2637-972e-39e3-af43-b98edac485a8 | 3.28393 | -60.61078 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f495e735-13c0-3592-96b3-65976b4842f2 | 0.1448 | -60.39766 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 79763e29-9c45-3cea-93d3-fb214e0790a0 | -2.02477 | -52.10669 | 2026-08-29 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adb3a20d-0782-3650-b7fe-dfb77c9a601d | 3.11186 | -60.70914 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e2475bcb-e423-3751-84a3-83d9cdb200bc | 0.13911 | -60.40612 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf057473-0731-32d1-8497-e2c1487f07c5 | 3.10853 | -60.70966 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7968d106-59d8-3380-8188-871163b818b5 | -2.59826 | -49.33862 | 2026-08-29 05:33:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bcfce96-0175-3141-ae8c-3569df793d4f | -2.02411 | -52.111 | 2026-08-29 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edd04ead-8402-385d-a640-241e790dd1c1 | 1.32079 | -60.71636 | 2026-08-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d858c7-4478-37a0-bc2a-eff5abe1feac | -1.25445 | -55.70808 | 2026-08-29 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e39c15ab-8de7-3292-911d-21f4e139cfcd | 0.13853 | -60.40242 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18a8ae33-5812-3d98-a9cb-dab7d1ea4326 | 2.41079 | -60.88007 | 2026-08-29 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 284868a7-298b-3435-8e12-5e9eeaa44225 | 1.65551 | -60.13859 | 2026-08-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9561b6b-8c25-3cb5-b076-3b8509963246 | 3.11131 | -60.70564 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3621cf5e-ba28-3d42-ae66-3f64743e86e1 | -2.02233 | -52.10719 | 2026-08-29 05:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07376877-fa3e-382a-9c66-63723ceaa67a | 2.51706 | -50.85055 | 2026-08-29 05:33:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9b4fc1d4-5585-3aca-82fb-c8af49930026 | 1.32751 | -60.71531 | 2026-08-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ebd23cb-d441-396b-a066-ba3df03e7481 | 0.87746 | -60.4854 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b96a72c1-1e46-3b44-b85d-1a07f2713964 | 0.1962 | -60.50303 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f403ab-8180-3836-a7f0-ecfa9bae9a14 | 0.14822 | -60.39714 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84ad043d-3f93-3ce8-a21a-73a4662d0f8b | 0.87846 | -60.48566 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d9a65bc-419b-329d-af62-a71de3a9a3a5 | 3.28448 | -60.61429 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c96a52c-493f-3017-a69f-453dad112af0 | 3.23538 | -60.13433 | 2026-08-29 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff7e1355-2467-35e4-9f75-340b1028c231 | 2.41412 | -60.87955 | 2026-08-29 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d36e56ee-50ef-3505-a155-dde70fe3a3bf | 0.14137 | -60.3982 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc9785c2-a8de-3fed-a718-f85626348edd | 0.14195 | -60.4019 | 2026-08-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee443ba6-d26a-3264-950e-77003c258b3c | -1.46889 | -55.53349 | 2026-08-29 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86f83372-0413-3590-9a88-4f10848572d0 | 3.10798 | -60.70615 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76219b13-9499-3fbc-bedf-55e4682244d4 | -1.6346 | -55.1228 | 2026-08-29 05:33:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a775add-a2df-3d60-89d7-e31eb43366a0 | 3.28726 | -60.61026 | 2026-08-29 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb353108-c9e9-31de-b8ab-114ff6920c01 | -6.95417 | -58.95583 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4916562-ccf6-3317-b7ef-406fab27163e | -7.48696 | -61.40271 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0c576d-5a48-3257-97c7-2aeac961cb8a | -6.77723 | -55.66087 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 7c0c4f6c-8438-3b9f-af78-3ad8f3a9fd65 | -6.00011 | -57.83128 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5415aec2-8ec9-3b62-aed2-b8e1e1b3e850 | -6.17101 | -57.77906 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b428edc-c7df-319e-8304-350a30863ed4 | -6.77186 | -55.6655 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ba1e71c3-f4e2-32a0-b5ac-a2b2cdb96d90 | -6.77101 | -55.67143 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dfac402b-f8df-3581-9227-0cb52c9671ee | -5.09264 | -56.14574 | 2026-08-29 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db466f9-13ac-3f48-8e8d-08ffc449d1d4 | -6.54355 | -55.24262 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f421998-6687-3288-bc98-fcb874b0e224 | -6.16124 | -57.78606 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c53bda82-a381-3111-bcd4-8f1bb1acf3f3 | -6.16321 | -57.80319 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56d0a1e8-4983-313e-8c94-3f2c60a6bef4 | -6.76645 | -55.66746 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29cbe198-efe0-3015-9b40-58a1abd01ea1 | -3.61799 | -59.77001 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37879049-0b16-36df-89f4-ca72f54b9ec4 | -6.72644 | -60.01586 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04ef449e-ff4a-345a-8c17-cf3fdb4af313 | -7.51029 | -55.30397 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a731e37-f87b-32b2-b04c-573f0353500a | -3.90961 | -60.94682 | 2026-08-29 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1cd04ea-405e-3fca-83be-5247ac34967d | -6.93807 | -58.95351 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 472f9cba-b1f8-31f8-9412-b97c4b478ae8 | -6.84543 | -59.94251 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e557d9-8b8d-31d3-b95f-7f9bac8f02f7 | -6.58426 | -55.43755 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8830056b-5629-373e-9a2b-6457d2e763af | -6.26409 | -55.4221 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c8240670-aa27-3b9d-877e-67239c801d5e | -6.7585 | -55.65121 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12558a90-6990-3540-8fce-a11ecf00f1be | -6.75809 | -55.65412 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8db1e9f0-0f01-37fe-ba7d-62569d22a518 | -6.77091 | -59.79154 | 2026-08-29 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1096b164-a2a0-37b2-931f-3dad15138cdf | -6.85085 | -59.43522 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 731cd3cf-cb11-37de-9d6a-ae08360a4e28 | -5.88994 | -57.75499 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6370d313-d268-3e60-9787-22520927434c | -5.99504 | -57.68445 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6dd77b28-810d-3629-ac62-ce89e69a87fe | -6.16612 | -57.78254 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 884d2df5-66c8-38d0-a257-a17eb2dac6cb | -6.82615 | -59.57579 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db971df8-e8f3-3035-abff-26632b904fb3 | -6.88345 | -59.40638 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3740a17a-5fd4-32f2-8b0d-483256546078 | -7.49194 | -55.28247 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb2818af-0f34-3d0d-9a02-fd2d31b1ae47 | -3.93957 | -59.33081 | 2026-08-29 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73baf597-e7f6-3739-b0f0-8150c3f095b3 | -6.76771 | -55.6586 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a17fa99-afb5-3798-89f4-9a51bdfc4adf | -5.88393 | -57.76621 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7238a15e-bb59-3498-8763-8ecdf4fd72b1 | -6.7834 | -55.6909 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3b890b3-bc75-3989-9e89-064125a90add | -6.91068 | -59.62974 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fb15845-831d-3390-8422-d1d472923df8 | -6.93405 | -58.95291 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afe0a7bb-16bb-3399-b2b8-52d882f14354 | -6.17472 | -57.78386 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecec5311-12e1-3f71-b832-04f53f9569dc | -7.50508 | -55.30326 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e82a0244-5316-3e85-87e8-563b94288999 | -3.15876 | -54.62698 | 2026-08-29 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16a7ad96-bbaf-3d7a-a721-2f7a65bb69bd | -6.77143 | -55.6685 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9765f6b1-9464-3ae4-93d8-cd62c5473c4b | -3.42785 | -52.77476 | 2026-08-29 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da69b587-6091-3a28-b125-2d9339f8df0b | -5.29385 | -50.94005 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e331d32-4ce6-3fc2-8063-110eae3fee36 | -6.75153 | -58.72231 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45455349-ffed-349d-afa6-14a9367f8bd6 | -5.98579 | -57.68742 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 113829f2-4bdd-302e-9be2-f9526a2e37e2 | -7.51506 | -55.30793 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f087da7-9670-3a8c-8664-269fad40cc82 | -6.58383 | -55.44053 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b04ff5-91a8-3a9c-b15d-e8f682469f9a | -6.76568 | -55.67054 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 058a8f61-8a08-36ab-9427-7784243a2b50 | -7.51592 | -55.30158 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 928dfc18-c6ae-358c-9885-5548a5e6fdac | -6.58341 | -55.44351 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961a4b58-456f-3c4a-a7e9-0256ff36cfe4 | -7.34646 | -55.16756 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84e6ed0d-0892-3ca8-81ee-bb76d2c13b06 | -3.5168 | -59.44356 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b713cf2-32af-3d17-8385-fab3f38d59f0 | -6.78109 | -55.6702 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd040cdb-b8a8-316e-bf3d-15d2c23b6938 | -7.51633 | -55.29852 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0b6dec7-9d63-3403-85ee-384a842571b7 | -7.50943 | -55.31039 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22345084-d204-3c3c-b00a-b9b905bc1d70 | -7.55199 | -61.30623 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a3e9392-374c-35cd-b8c5-d8248741edde | -6.77564 | -55.6749 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18923b22-0946-3c9a-af62-3537714bb05a | -3.15918 | -54.62408 | 2026-08-29 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README59.md)
