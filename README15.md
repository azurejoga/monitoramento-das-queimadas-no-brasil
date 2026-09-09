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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74a9b6fd-d7d5-340d-a865-827759b2f124 | -6.75874 | -44.58003 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c19dc2b5-dd73-3ea3-941b-c82a76a3cceb | -5.76325 | -45.07919 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e61250d-d36e-3df9-852c-65efca94ec91 | -5.4934 | -44.69286 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18d89d8e-c499-38eb-98f7-27533d149360 | -8.09205 | -45.68015 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79312a26-24eb-3d11-85fa-9d6079995427 | -9.69431 | -43.49353 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 237cb14d-beda-32dd-8327-03a5694f7634 | -3.96929 | -47.58684 | 2026-09-09 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c79e5fbf-8592-33d9-bbec-373c97440e02 | -10.46652 | -40.57403 | 2026-09-09 04:25:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 088a0e18-1b8f-3504-a681-427943e5159a | -8.41645 | -46.89415 | 2026-09-09 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc4ffa57-48d5-3eba-8f29-8ec602091042 | -5.21379 | -55.99036 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f5ebaa6-e69c-3624-b719-96ff506c04a4 | -7.68524 | -44.31593 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbb0b546-2413-318b-bf26-6f88d1cff4ad | -6.25264 | -47.34642 | 2026-09-09 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5640b8c7-4605-3c16-ab7f-f97890d4669e | -6.99511 | -42.0521 | 2026-09-09 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4c73be73-ca58-3cc7-903e-5dc09aa4421a | -10.2403 | -45.21969 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d65147f3-87ec-39f0-87f3-ee49017501de | -7.53432 | -44.99076 | 2026-09-09 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc75eedd-440d-3e99-9207-536e0b90de98 | -3.36754 | -50.39797 | 2026-09-09 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8331745a-b57b-314c-b672-b59ed5b73fae | -7.52435 | -45.92739 | 2026-09-09 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acba7f9e-a8f6-30eb-abdb-5e75983c3fbb | -10.58395 | -45.74729 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4abdb2e1-1ac5-3d35-ae24-be660c264581 | -11.26311 | -45.69732 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8271b597-490b-318c-9434-7cb846fcc5cb | -7.19084 | -43.61916 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8dcd55f3-3944-3e89-ae97-cf7df3a3b1b2 | -5.77829 | -45.07383 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 502bcd90-7a06-3ed0-bd00-2dab82e4e94f | -6.36244 | -43.59067 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d699d44-bee4-3ebe-9107-e80966df06ac | -10.99208 | -45.08913 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6970481f-8234-375d-9442-3e33508dcaef | -5.60778 | -44.84723 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fe1b010f-e9d1-3c73-9ca9-b829f7611441 | -11.18637 | -40.88777 | 2026-09-09 04:25:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a07da47-b211-3bce-bbc1-d0aca0bb2c93 | -10.18138 | -42.2241 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75d55361-f59e-3a72-b622-2bf468395a8d | -10.73572 | -46.01328 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 74eb6939-b8cf-38a5-9a7a-2bb37e22ecba | -6.62219 | -42.22814 | 2026-09-09 04:25:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dadb544a-b4f6-3a1c-b2dc-2de27afc8735 | -5.82289 | -53.79688 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae87a820-ca0c-301a-b12a-670d6a7fc465 | -5.60592 | -44.84378 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 15b31cf1-7f02-336f-a534-0fa80016e019 | -6.36133 | -43.59763 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ad70f2-e8bb-3f71-b530-b119f3761048 | -10.74722 | -45.96518 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4767110a-788d-3751-b008-842450f5123e | -7.67424 | -44.59847 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71b5e408-040b-32bb-9db7-be74ab0ba431 | -10.75344 | -45.97006 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 306f4ccf-0193-3207-8627-7d0bfa14e6e3 | -5.76264 | -45.08296 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 324572cf-133d-30c6-8b9b-2a89ddbb1435 | -3.79997 | -52.40845 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8507f2e-8bfd-3a04-9d59-056a2651100b | -6.75933 | -44.57643 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b32479e-55a2-3423-b116-a4602bb4b854 | -9.26063 | -45.65503 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3168a42d-380c-3746-931c-6f01dc35150c | -10.99266 | -45.08557 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7268a0cc-9260-3a38-afa3-af348e55b7db | -8.0996 | -45.67751 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28831a51-61c7-33ce-85ad-3842e91af835 | -5.41727 | -44.79443 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9709fb91-4367-3aa6-a017-074074d8b0f2 | -11.4824 | -42.24179 | 2026-09-09 04:25:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ba62ee7-c84d-3be5-96ad-06c945c117cb | -10.58796 | -45.74417 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805e4ce9-32d3-37d2-b9dd-357bb9cee769 | -7.19306 | -43.62666 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80374b32-ec9b-3427-936f-785b8fd1f3d7 | -6.76049 | -44.56922 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a7591dd-564d-32de-86ba-58df898564f8 | -9.72149 | -43.47269 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c78e359-40ac-3dc6-bb71-7215364d0f52 | -9.70151 | -43.4695 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be705f6e-a519-359d-9ffe-68ef9a3ed542 | -6.52384 | -44.02147 | 2026-09-09 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1173593c-7f93-3c38-ad81-4304891d8dfd | -5.80327 | -53.82331 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 779c9625-4f2c-3faa-a1a9-3332ba4ec5a0 | -3.54901 | -48.18719 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d420ba9-88e6-3d81-b19c-99b7f418197e | -9.98312 | -43.43806 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80ee1978-4569-3f0c-b392-bfecad591042 | -6.8637 | -46.01186 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fee5f37-4ee9-3108-9b17-f10b32b490ab | -5.77889 | -45.07006 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea264f42-b45e-3f69-a351-1896a21167d2 | -9.26003 | -45.65878 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3797c056-6e0d-31fa-a0dd-974f9aa94341 | -9.69705 | -43.43279 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e9881e28-db2f-3465-884c-c2cab239283f | -9.74477 | -43.51216 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77f4dc33-3168-3969-ac8b-654a6d47c31c | -4.38274 | -55.04885 | 2026-09-09 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c78a9f7d-7562-3efa-980e-29114aded0c8 | -3.54467 | -48.18213 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e0c5008-838f-30c8-b331-db5c59c13a35 | -10.17796 | -42.22356 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 984620f2-c5a5-3ed6-86c2-acba0aee3bad | -9.77694 | -43.50292 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5410d2b-e408-3970-afe1-6c3f17bbf3a1 | -7.19029 | -43.62265 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f808360-eaa6-3d76-95a8-0b9319a2c6d2 | -7.68467 | -44.31946 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 338f1735-c701-3c97-a2b6-90d859e04d70 | -9.74751 | -43.473 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73c02bc2-f835-380e-bbf7-a14f01f97adb | -5.81073 | -53.81575 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3539bbd8-22ec-3b55-aca0-f60a99faddba | -5.60533 | -44.84749 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0bd02c0f-a181-3774-9d73-73020464e7de | -6.87369 | -46.01765 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39bed2f9-dab8-3493-9a06-7790b895cd0a | -7.9953 | -47.73446 | 2026-09-09 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b6386a2-8a4c-301e-a712-19ee22dd52ee | -5.81149 | -53.81144 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42dead26-d66f-3440-93e4-df2ba8d03697 | -11.18271 | -40.88721 | 2026-09-09 04:25:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5b26edd-4c39-322e-8a99-73ae29fe97c3 | -6.03412 | -42.63764 | 2026-09-09 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f6ebf7e-5c69-349d-b899-12c6d064ea3a | -4.01966 | -50.44418 | 2026-09-09 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee27f9de-b8cf-3b44-9115-89a4e6b2c9ff | -6.87079 | -46.01311 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3af4412e-c0da-3939-8856-42e1d0a09572 | -5.77543 | -45.06952 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93c26600-9560-3fe2-82a0-fbd767c7b5db | -5.76956 | -45.08403 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0039a27e-4ef4-31a8-8009-c6f35e8b4bb8 | -6.1583 | -44.65993 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6631f66-6098-3f7a-911d-d08080f44eac | -8.09676 | -45.67314 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fe3d233-beac-34ae-ad78-52d1b0c97f5d | -5.98674 | -52.29391 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1440d78e-3ed6-32a8-b0c2-6197afbe8a55 | -5.80193 | -53.81095 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b7627f7-b5c0-34d5-ae51-64ee7f72e294 | -6.16403 | -44.64592 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b671d48-593d-3cd8-8253-7d1facbe064a | -9.69708 | -43.47598 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3cc0a8e4-7107-3b7e-8443-93f2c5e496ef | -9.77691 | -43.45969 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a628646-7c4d-307e-91a3-01020835f2dd | -9.71816 | -43.47215 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28f39353-81e1-3b19-ba55-5f4e42db26aa | -5.7178 | -46.19271 | 2026-09-09 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5aab6423-1f28-3c90-9265-bb34b7a2df7a | -5.81377 | -53.81329 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 867ac47c-5ae7-3d05-9695-227e91783a52 | -9.70869 | -43.40223 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1b78e6c6-fd06-39ab-8ef6-a8742fd6567a | -9.26345 | -45.65937 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0912b5d3-8044-3a03-b6bb-b91465836f08 | -9.7719 | -43.44808 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a60f88-fe2a-3462-ba9d-562bf503924e | -9.70207 | -43.46599 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 169374cf-a81a-302a-8037-066c4a014cfe | -9.69265 | -43.50407 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ab00d06-aea4-3839-9c05-28591ad97c92 | -6.36521 | -43.59468 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1e9789a4-8e1b-3d28-b089-af079e4accd5 | -11.3952 | -43.92048 | 2026-09-09 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff7743c6-3059-3a1c-811d-1d2e81fb280e | -5.42284 | -41.83818 | 2026-09-09 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 723c9112-f5d1-366c-b20e-a65d8b174aaf | -10.13995 | -42.13414 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94ec3ff1-2ba4-38fb-aafd-7ccc55d57228 | -10.36614 | -45.17432 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0a1c95c-34c5-3011-934b-7e8eb6b047de | -8.09739 | -45.66935 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c85fa4d-45f0-3f8d-b453-e9371f7c0a5d | -4.37711 | -55.04245 | 2026-09-09 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 864eb118-9f9f-3bc1-8a38-446505c7bd7d | -6.15947 | -44.65265 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fd5eee00-7cec-3df3-a777-865576109a89 | -11.48298 | -42.23795 | 2026-09-09 04:25:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 659a4bb8-0f26-31fe-83b4-71334d95d03d | -10.69572 | -46.00326 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edd2ab2b-e7cf-3584-92b9-01214e6165d2 | -9.78681 | -42.00002 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac6fc58f-9362-390e-a8a8-337b206245d6 | -7.53092 | -44.99022 | 2026-09-09 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
