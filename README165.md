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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f662649c-d7cc-3534-9fc6-5804cb9d4797 | -2.9236 | -58.52481 | 2026-10-09 05:04:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f304f995-6c06-3e47-8de4-efbcbde63e05 | -4.1177 | -54.01685 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39438d2c-5e7e-3673-be2e-cf817aa7ac9e | -6.43933 | -52.67319 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2b3c984-65ef-3742-971e-02bbbd289c24 | -6.21751 | -44.1497 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15780fe6-b8a6-3bb4-8c70-f17272b9dac0 | -5.29447 | -60.09161 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dac7908-c94a-3c36-b4ce-a35164f4364a | -6.10338 | -55.70092 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb3c8de8-0835-320d-8276-9c3f8774ba1c | -3.02221 | -54.76068 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73f404de-32b3-3bed-a673-86e3e73c1f4e | -3.26757 | -54.04891 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab32357-e9f2-30b5-ae4a-90f9f671de5a | -3.08079 | -54.29028 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14761234-2b91-3fd5-8de8-ec6b149cd746 | -7.75856 | -54.95329 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b391e59-3552-3748-91c9-e62eb01c107f | -9.69145 | -58.08565 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca8bf228-259b-3424-89a7-52bf2136f8b6 | -3.77553 | -58.58846 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cc60f65b-003b-3dce-8615-56c89fe9ef2d | -7.51813 | -47.33154 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f77f09a5-3746-39cf-b576-f020a952cff6 | -3.71348 | -54.23515 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0996197b-9c4e-3f2d-a1d9-072dca942841 | -3.08547 | -54.30613 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96be84cc-bb6a-305a-80dc-5393a97d0cb7 | -2.91126 | -54.11273 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a49f8d0a-7d73-3686-9391-8b173e75f142 | -7.29051 | -45.41275 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad99d8da-0b95-34c7-8774-592ff377daad | -3.25673 | -54.02763 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 138480bc-b098-3b7d-bdd5-89268561a8ab | -8.69699 | -62.40787 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6352ea8-3f05-3f24-8acf-61a298b96c5f | -3.00914 | -54.75025 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 769b1033-3328-3c10-b526-e402be9fbd59 | -8.58257 | -53.10461 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78ef69e0-ca01-3408-ab2d-5167a3b49151 | -4.9486 | -49.41562 | 2026-10-09 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51546b4d-c592-3cd0-8f5b-be1544ecf340 | -6.48281 | -62.85682 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ead6876e-45d8-330d-8b44-a897d108fc1e | -4.63046 | -48.86308 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c61210d9-bad9-32eb-9889-30a63b1e6ae1 | -4.12539 | -54.255 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3b49709-c320-3f46-b689-295d6131214a | -3.00611 | -54.08347 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f48febe-a99c-3b1d-9164-88ba3dda6130 | -3.30152 | -54.01529 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fca65f04-6b75-369c-8b30-40bc37cef499 | -3.16801 | -54.73224 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a83a811-0e5d-3d8d-8410-0b794c53208b | -8.70235 | -62.40904 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4bc438a-01cc-3409-80a8-8f330590647a | -2.94518 | -54.16982 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d5b7b63-d24b-3511-b896-e124a5d0dc2c | -6.11399 | -51.7332 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0fe47e0-fdfe-37f6-bf3c-8d932b1fd1e3 | -3.12455 | -54.17672 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 80b2e02f-204c-3cf9-ac42-d220a02e52dc | -3.31133 | -53.86563 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6d92b0e-dbd3-3abc-a4c0-34db6c2e9ba1 | -3.01221 | -54.04203 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd3e2fd-e28a-3c6c-a0b5-d7cf513ad468 | -3.01471 | -54.09668 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe392866-99a2-3c2a-8f9e-3f4afaae3603 | -6.96468 | -45.27345 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c330c52c-90e3-32a7-910e-f1b7141b454d | -5.70699 | -53.45085 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c6bdf7f-cb4a-3ede-9aca-326cbfff84f1 | -3.5754 | -58.63453 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddee5487-adc3-3b40-bb42-575de0e0cc1e | -3.70733 | -60.54147 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5976e0e2-19a3-30fd-83ce-a19578af5b79 | -6.38546 | -45.94127 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be282415-a0e8-34d0-98ca-a0256623ec75 | -3.60244 | -61.6259 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4edae1f-aa9e-347a-b4b5-8fdd4c9516b5 | -5.25417 | -55.9193 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ec90113-c818-3613-9ab9-dc78c482f69f | -2.38855 | -57.89498 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b0ade07-5fee-3f86-bef6-19a287ad579a | -6.95992 | -45.27284 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8905c008-927f-3f8a-b64b-68f0f3894361 | -9.83343 | -47.45566 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf09dd04-92c1-32bb-b08e-a85227f0480a | -2.98699 | -54.06557 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e476eb7d-ec6e-38b1-92c6-4bc81b0b82f2 | -3.9335 | -55.80026 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81556156-8cd1-3ee2-a888-14040447ac9e | -3.55376 | -54.6954 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 647ee1dd-f318-3439-a6d0-7aea477adb4c | -5.69744 | -53.46744 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d37adcb8-908f-3c94-8ead-cdab1b44e12a | -8.58312 | -53.10112 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e711dd12-6fc5-345a-8237-620cfe74384c | -7.18641 | -52.61045 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da661338-6df9-3948-a839-aac34b3c79d6 | -2.57175 | -57.78761 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14d31b68-d18e-3a28-a257-0145859ae0f8 | -2.98681 | -54.08922 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ef18ec-2637-3c0e-b849-2e42edd93825 | -3.52883 | -59.34523 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd6daf3-46f2-377b-856e-3f5ae399d460 | -5.69687 | -53.47098 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcd88133-7c2f-31b2-8cef-b311006b6abe | -3.50338 | -59.26214 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e9cce9d-4c60-386f-beb9-c43a504e792b | -8.96229 | -45.17141 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 998ea29f-d134-3aee-857a-b158815e8bf8 | -10.94754 | -50.69597 | 2026-10-09 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72726ab9-dc1d-3fc1-8d68-d76233c4040b | -8.91534 | -45.22122 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d85d2b63-a368-309b-be55-dad7033912c8 | -3.80095 | -50.61306 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0d8ac5-e847-36cb-b724-a2106390523f | -4.04266 | -54.23096 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e32a951a-46a5-3915-95f7-92103cf7dc5a | -2.56625 | -56.17175 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a323404-4542-3ff5-908d-ad975afe711b | -3.05714 | -53.92328 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c280f4ee-277f-3448-8bf9-b2be5f41f7a5 | -8.494 | -54.62598 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2af8f34-8b69-339f-841c-c2c0d19f790b | -3.56536 | -54.66849 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8c472ef-a6ea-3631-908b-3822b4c5cffc | -10.32182 | -46.60597 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77a15659-c5eb-3637-814c-8d3747da5ff4 | -3.30097 | -54.08559 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0747f078-3f8b-3a9e-86fc-466a78136558 | -4.5839 | -54.94918 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e937be32-3a3a-32e1-894f-d934ee4ea73f | -3.5898 | -54.68736 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4979af5b-6b4f-3269-a625-cde71a3e9221 | -2.471 | -58.08003 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aba06bd-6a5a-38b2-a072-e706d602fdd9 | -5.96815 | -55.3675 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8aaafaa1-85eb-3aee-9381-b72c802305bc | -6.31042 | -54.79966 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43cd675e-1588-3a79-8d45-295cb62187d5 | -5.09893 | -46.22468 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee7aca20-5be7-3f90-9478-1dcf74a16b27 | -3.94565 | -55.84396 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cec15170-a317-3280-9f11-ab6c3ec9336b | -3.00646 | -54.10328 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef2cc9f-dc71-3194-beff-b33c89e1cb74 | -6.01166 | -53.48842 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f4bb9b1-6d11-32de-a60f-8ab06eda241c | -5.67499 | -46.36053 | 2026-10-09 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e6b263-741a-39e2-bd17-50eb796ccca5 | -5.09642 | -46.21924 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4e4cdf-5c95-3da5-9e29-72d896544aca | -2.99275 | -54.07437 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d6a7d54-0daf-3474-aecf-22e7acdc9cba | -5.96257 | -55.37898 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e23d52b-cd9f-3e8c-8624-d4659886bf8f | -6.40226 | -55.27262 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcc5a400-715d-3d60-bdec-6660bb7ac2e5 | -3.52798 | -59.35042 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 086cc712-35e2-3913-a0e8-32c0e8d66729 | -3.11468 | -54.17114 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3334621d-433f-3150-96f4-20965a061dd2 | -4.38769 | -55.4489 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99275c8b-1f59-3556-805e-e556ebff0e8f | -3.00396 | -54.11867 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8c3fc00-df66-3b86-b2fc-0aec4110be1e | -3.28885 | -54.00541 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e376fc9-0ae1-3292-b5ae-7b4432ce388e | -5.85371 | -53.45552 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a30b925-88c2-3aa2-a55f-53a02b3ea0bb | -8.73332 | -45.13678 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3efc6763-c8cc-3147-96eb-280311c8b5c2 | -7.06922 | -47.39192 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef63044a-e9d2-3f6e-9e5f-6bec6af5517a | -8.99378 | -47.73814 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4ddc955-42ed-3a3c-acc3-b79d642fb713 | -3.2989 | -54.05389 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd913d99-27e2-3266-b14a-d44ec0e9c3c2 | -3.31405 | -54.04847 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa17571-7919-3b5c-a595-a070d89ed402 | -3.30474 | -54.67039 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdba9d07-1fe5-331e-ba95-63cb50e32dba | -5.90888 | -53.89138 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24e1796c-cab2-3254-9e1d-b021c4359a12 | -2.86714 | -54.20535 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bfa9a87-bee7-34ad-9e90-26477a5bdf99 | -4.97872 | -46.04253 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 896965c1-158d-3a4e-82ea-1f932fcc3b1e | -6.3063 | -54.80303 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 219e1c67-0947-3e91-be92-dd279c25dda8 | -3.25611 | -54.03145 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c5330c5c-c883-3969-b090-da61e199dd65 | -8.74773 | -62.62507 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e6061fb-3c1e-33fd-bea2-396afcd94753 | -4.29041 | -54.77744 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README166.md)
