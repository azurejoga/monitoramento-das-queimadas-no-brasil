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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bae1e81b-1030-39d7-be58-74a607d3c4e6 | -3.73531 | -49.05387 | 2025-09-25 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e903e10a-c6ce-3858-aeb0-1fe7ca191a83 | -5.39119 | -42.28997 | 2025-09-25 04:32:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3ac490b6-c041-39c1-9d16-f7d34c81ba2f | -1.22492 | -46.20554 | 2025-09-25 04:32:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a681db79-0626-365d-ab2c-1146e087cbbb | -2.44313 | -47.18332 | 2025-09-25 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 210b5b26-ebed-3a5f-8b03-e0ad1cbbe2fa | -6.55475 | -43.83662 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f921c83-5b1b-318e-9909-3bd849d8210f | -7.17617 | -42.23467 | 2025-09-25 04:32:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 41f8f394-06e5-35b2-af1f-d2f963e50aa5 | -5.42645 | -41.32368 | 2025-09-25 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7afb0f7f-aee4-3177-b12c-854362cdd299 | -2.56925 | -49.11811 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ae916c-510a-3cc8-8133-de457ffc7f14 | -5.06306 | -44.32006 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 629858ed-9a79-35b4-ba3a-d3c43e95c220 | -6.42822 | -43.08002 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 623f0209-9b9d-3fd0-9178-f20fe55c88c8 | -4.75192 | -43.25377 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d97606-c1c7-3b9d-852f-ba8adfa04e55 | -6.10176 | -43.96434 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55bd8475-04d0-3441-8e85-076b62eb4cca | -8.0715 | -42.94886 | 2025-09-25 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e81330aa-bf48-3c18-91ec-5f29ee86d6fa | -2.44532 | -57.94302 | 2025-09-25 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08918a9-f85f-3587-a02f-01d950386aae | -5.56724 | -43.60339 | 2025-09-25 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bbfb193-7b96-3e1b-8bac-1c575aee143c | -2.70538 | -54.65625 | 2025-09-25 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8854394e-9c1f-31f9-a04f-0fd31cdd7283 | -3.79352 | -41.72897 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7305d0b2-4b9a-3859-88f3-b471e216ddce | -5.78557 | -42.81036 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 50b4151a-aeda-3048-a9ad-277af1872a39 | -5.60627 | -42.98892 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4a509de5-1e37-36f6-83c3-634cb4a30f49 | -6.41475 | -43.0885 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 792e34f2-a6b4-3b6b-911a-c22158ed1016 | -7.99095 | -43.58241 | 2025-09-25 04:32:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d48712ff-740d-3275-807e-f5f3e1cb9d3d | -5.24352 | -43.1396 | 2025-09-25 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76fac19b-bd77-3e0a-b387-3d1f709b8c4d | -6.73303 | -44.04524 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdb865f2-d13d-3b7f-8fbb-44dad1ee4552 | -5.95926 | -42.90729 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b932cfae-cd33-3f0d-abc7-3ba0f26f0252 | -6.07269 | -44.08006 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce9560cf-60bb-316e-a85d-14ba323ce670 | -6.45768 | -44.20419 | 2025-09-25 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d2efadc-a27c-370f-a90e-41e92b5ad0e8 | -2.3594 | -48.88949 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5c615b-f9e9-360d-8964-d965c23a44d2 | -5.95577 | -42.90316 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 44b7081e-b215-379d-9d0a-8f2866ba9ae3 | -3.39519 | -47.49844 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d62b25f1-4d1f-3b61-a941-ee2d46fa8c76 | -6.30755 | -42.53929 | 2025-09-25 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8925028-3cf0-3376-915c-6dca3ac04b26 | -6.26103 | -43.44666 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64ba223-c614-34d2-ae32-babbae9d5ef6 | -6.32286 | -41.88343 | 2025-09-25 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8555435f-bb81-3a86-a47b-a9e935976ec3 | -4.46256 | -41.92169 | 2025-09-25 04:32:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1f18bd1-0700-3bf4-85a6-3301f34945a5 | -6.89094 | -44.76105 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 300073b7-7a13-3e25-aa16-c9ff4c2bbedc | -3.94 | -49.40153 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbaec0c4-b75a-3591-a48b-e07d5863202f | -4.34525 | -46.46693 | 2025-09-25 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be21527-3e54-38da-abd3-3794ae466912 | -6.69821 | -43.52943 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7d06189-82f8-3891-8003-e1bf724c2ec8 | -5.94326 | -42.93312 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60143a08-8180-3736-a17c-d5ea2ca8d771 | -4.7366 | -44.42454 | 2025-09-25 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0e0c0533-ea92-32f9-82cd-98e15280b28d | -7.4534 | -41.90151 | 2025-09-25 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3350120f-566b-3a9e-9413-73d2f3b94b00 | -6.56986 | -42.06359 | 2025-09-25 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 502574a7-80a0-31bf-931f-2a77cad8b874 | -4.04211 | -49.53218 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fa4fa21-95c1-3928-96f0-cf8140bcad4d | -6.4277 | -43.08348 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 33c3143a-21ed-3b3e-8804-90730d962aff | -4.28933 | -48.26144 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d235f328-e37d-3ea6-a87a-9decc7991fcf | -3.30121 | -42.17267 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1589ed9c-1eb1-3950-adbd-cbff65c6cb30 | -5.5153 | -43.87297 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32d1b81a-8947-377b-b07d-b4f8df4fbed3 | -7.11091 | -44.48653 | 2025-09-25 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b62ff700-d508-3111-813d-cb150a9638d9 | -6.42078 | -43.07528 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ea984a8-9fa6-3206-b4a4-9e83ae8750fa | -2.19504 | -54.46927 | 2025-09-25 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e7100b7-0530-30bb-9cc1-28615b6f7e30 | -7.59086 | -42.32672 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a406cab1-1ac3-35d4-a9d6-332693a60f9d | -3.7912 | -41.74434 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d736848-c492-3b6a-a234-3c53401ea352 | -3.61503 | -38.76586 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de76e98e-9673-3d46-b0a0-76b84e428bd6 | -4.78302 | -43.20451 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66799a1c-aa2b-3ee3-ae4b-60b9806e262f | -6.0764 | -44.08072 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38bf6f05-b51c-385b-a6e8-2fdb17f60a59 | -2.96033 | -48.59683 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| befe292b-95a7-3afe-9e84-42b4152b6add | -5.31861 | -42.73346 | 2025-09-25 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51f638ce-1bf2-395a-8b10-ed14f0412899 | -5.93274 | -42.92123 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7452706b-2d28-3ebc-a0fa-3d5f69eb4936 | -7.98654 | -43.58295 | 2025-09-25 04:32:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35be295b-185e-3d2a-9431-2572171d1d0d | -2.98887 | -49.28559 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c2450c2-280b-383f-a5f7-aa4ce180c900 | -3.31374 | -48.72517 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dca9223f-f6b4-3899-a418-050456317e8d | -3.7453 | -38.95187 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5494ccad-3f2f-3792-90bc-0e800a85724e | -7.45403 | -41.89716 | 2025-09-25 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fca6adf5-7582-3232-95b2-d44f8cd14870 | -7.4584 | -41.89782 | 2025-09-25 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5682509f-4469-368f-b054-5e87362a41aa | -3.69331 | -49.56365 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f08771d1-6a63-3b6a-93f3-312e863608be | -3.08571 | -52.91857 | 2025-09-25 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4fa1e3bb-3d37-3e25-83b0-646e77f3344c | -6.69521 | -44.61741 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d81e754-7bae-3736-8050-525ca37b1c27 | -5.52652 | -43.8748 | 2025-09-25 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fea77573-df8f-3948-995a-fc474ac11bed | -5.79138 | -49.13732 | 2025-09-25 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dced1b5-1344-3df6-931a-024e95dc6008 | -5.05726 | -38.07522 | 2025-09-25 04:32:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae58dd5a-4451-353b-b5c2-841527eac992 | -6.99226 | -44.71001 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb819b7-134a-3682-9b7c-57d987c1c485 | -4.80297 | -43.53286 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9466a58a-3829-3645-9a67-96d67599c89c | -3.69902 | -49.57228 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fcd21d2-4566-3bac-904f-a8a205adb3c1 | -4.89252 | -44.95414 | 2025-09-25 04:32:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 301a9890-a9a9-3139-ac3e-789a192a9e3b | -5.60268 | -45.35987 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7268d69-f9e7-3a9c-8ff5-9887dfefdbc7 | -5.77703 | -42.55658 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 52a7e715-b77b-313b-9ea3-de337d5f628e | -6.43168 | -43.08406 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b2ce6894-d66b-3b68-9c93-7270bffb3141 | -4.24585 | -53.55284 | 2025-09-25 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7783bc3-c40f-3a0e-bc04-eca58419b041 | -2.44803 | -57.94536 | 2025-09-25 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9fb2f05-f29f-3ac4-adf0-b9202451eafe | -3.77979 | -41.73483 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b72f758-5367-3ecd-a522-ae95de7cd3f9 | -7.16195 | -44.49858 | 2025-09-25 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6408cad9-76a6-3edf-b545-bee7991e707e | -5.75186 | -42.61385 | 2025-09-25 04:32:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 53963f81-6626-3083-8afe-2cf521b2b8ed | -6.57754 | -43.65154 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64f18c25-a2fb-3ede-88de-7de5475243f0 | -3.61837 | -51.80111 | 2025-09-25 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ac2d828-e53f-3762-a5e2-92e46abf70cc | -5.09231 | -47.48118 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aad1c201-a205-34d8-b2b9-b2362cf24b53 | -6.20303 | -43.9358 | 2025-09-25 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62f1fc95-872d-3414-94ec-a56616e44a28 | -6.07392 | -44.08336 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 917fb58b-1426-3cf6-8e55-136bf3d1baa5 | -2.92459 | -48.30465 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a9a9a85d-837c-341c-9a97-0e151d2592a1 | -4.78688 | -43.2051 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bca24d9d-d0c4-34bc-87a9-6ad533f8a98d | -5.82215 | -46.35332 | 2025-09-25 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9536847-39eb-32bc-86ca-3e2c1bc21a28 | -5.723 | -42.6124 | 2025-09-25 04:32:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f50408ad-b81a-3ce4-88b2-f72058321c83 | -5.53026 | -43.87542 | 2025-09-25 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 81a265b2-1a27-3338-a132-7840aa1b38f3 | -5.61343 | -42.99532 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 40eb482e-11f7-3df6-ae93-6b185789a702 | -7.65509 | -43.93567 | 2025-09-25 04:32:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e840ee78-9ee4-3cfc-907e-5b6cefbeeb88 | -6.13 | -44.44139 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c75bc129-f75e-353d-a92b-3df8b95767fb | -5.61022 | -42.98957 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 45e98f61-acfe-3101-b9e0-c8545fb28541 | -7.58905 | -44.44177 | 2025-09-25 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eed1b2a-3ff1-3d1f-a2c8-a115e2a751ec | -2.83101 | -46.72818 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2667cf9f-50e1-39e7-8544-d1ac038ff724 | -6.63752 | -43.82955 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f0ae83b-3f22-3624-ab5b-6a2e6fcf8707 | -6.22861 | -44.66108 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b6a3e9b-4bb4-32c2-8731-5a6fde90dfef | -3.82757 | -50.96794 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
