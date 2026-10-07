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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53f60c15-216e-36d8-a914-5fa91e01935c | -3.85837 | -55.99496 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 52cc3259-ef6d-34a4-ace3-7d096899ec55 | -2.77165 | -54.08073 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 91366b97-37d2-34d0-a50c-a70cb3ecb83e | -2.60061 | -48.25731 | 2026-10-07 07:18:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 903f5cde-ba9e-3baa-b6cf-1a5b250dc0cf | -3.47282 | -50.08163 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 988e823e-0eb4-3083-9991-84f7ea5cef81 | -3.58746 | -54.56527 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93ca2ef6-2b4c-38e0-b387-999b28ff5481 | -3.9952 | -56.24852 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f12e6593-8735-345a-a0c0-41e36359c4b1 | -3.00738 | -54.11658 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 01a5088c-8e33-3b34-9e1f-67940e6df49c | -5.7266 | -45.15494 | 2026-10-07 07:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 4189b0c6-5be9-3aae-b447-3f0be5e883a5 | -3.21787 | -54.30236 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54632a76-4c61-3655-8cd5-175a1e133fc9 | -2.99119 | -54.1053 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 33710ded-624c-30f3-aa2b-230a463fda2f | -3.93874 | -51.01762 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e65a92d3-0e56-395c-9363-e37f3414c610 | -3.50632 | -54.6634 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1db1d20b-0c15-39f3-a608-bd5a7fb881ec | -4.92357 | -55.86603 | 2026-10-07 07:18:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2fb29ec9-acbf-373b-b1a1-056ffe658e51 | -3.48357 | -50.08329 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c654c8b1-cc5a-3634-b009-99076ec3e136 | -2.9381 | -54.14425 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a360d47b-3b51-31ed-b9eb-d88dba30e849 | -1.79882 | -57.10595 | 2026-10-07 07:18:00 | AQUA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| e944a0c5-9a46-3491-87ce-516341cd4586 | -3.29767 | -54.03505 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f2e8f835-0eee-3896-b256-f68395245f51 | -3.56213 | -59.47729 | 2026-10-07 07:18:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 426fdc4a-44de-3906-b6f2-5ff80b2457ab | -3.22885 | -54.37194 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a870db7-4ee7-31f5-830d-ef6c9de46932 | -2.98016 | -54.04368 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c36fef2-5689-3d15-b34b-4717564e3888 | -3.59621 | -54.56655 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c6f4110b-be5e-3b58-ba95-725db95be34f | -2.76638 | -54.11551 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 71ea04f9-b7a4-3ac0-9bee-695b80678940 | -3.00606 | -54.12529 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 57285447-7a47-3f8c-b38d-7dc9bcc09048 | -3.0826 | -54.29352 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a7665c95-35e7-36bb-aae3-531eef2a684b | -4.56422 | -54.94794 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 983c6b74-8f3e-3fdf-8bd0-531f98a4246d | -3.99374 | -56.258 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 12ac9a9d-98ad-3f7a-8a0c-c4d1ed698bd3 | -3.1242 | -53.75882 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 17f8fae6-cb1e-3bad-adaf-7474e039dd6a | -3.0302 | -53.90607 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4d251604-933f-345f-b877-136e8b6a945c | -3.08392 | -54.28482 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 0bb86da7-43b7-37d4-8d09-0bcc6d3060dc | -3.4766 | -54.62337 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2d0ae7b3-1b00-3e1b-aac5-f012eaf19ed0 | -3.09266 | -54.28611 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| f0c10ced-e78d-3447-bf91-67084cb447d0 | -3.09135 | -54.29481 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fa334c25-a983-363e-9eb2-e9b2311fce1d | -3.28147 | -54.02375 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 47b997cd-6413-3e66-8c53-3b44cc8b17cc | -1.11905 | -54.1166 | 2026-10-07 07:18:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f76fb28-f4ac-363a-a50b-839bd75c5cb9 | -4.09986 | -52.0697 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1a3edf59-951e-3450-96af-59c9a728edfb | -3.28497 | -54.05993 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f9ca8bc7-9523-38d8-9fd5-0e70086a002e | -6.00288 | -53.4995 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 918bc634-6e2b-3392-b6d8-4ad9852c423c | -3.22661 | -54.30365 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f37703c-2da8-3e93-b547-474b0be40ea9 | -2.77645 | -54.1081 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3c7ac798-ad96-3435-be5c-1cbd04325476 | -3.7059 | -51.13303 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80b7a8f5-5b77-344c-9515-5933f1acf995 | -3.29155 | -54.01632 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 40e649ea-9ccd-3dec-ae25-25e4c148cde8 | -3.58878 | -54.55655 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bd9d3ac-46ee-3f64-94f0-e23dabb273fb | -2.9876 | -54.05368 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ecaa57e-0774-337f-ac70-fe40d3de1360 | -3.68076 | -55.94661 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 15cb3c7e-38a5-3b61-95a7-d44a779e4387 | -4.44104 | -54.97662 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 895ffdb5-24e6-3cd4-ad2d-55f1db86c895 | -3.58798 | -54.30164 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b6f02565-43be-39f6-bdf5-bfc9bc4a1028 | -6.0015 | -53.50878 | 2026-10-07 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df43a5bf-ed0b-3263-a118-e0c2bdd48049 | -3.55071 | -59.47557 | 2026-10-07 07:18:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2337bea0-980e-3d3e-ad46-1a969182802e | -3.51508 | -54.66469 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d30be863-2afa-32c2-bf8b-0e9749cdf4f8 | -3.2841 | -54.00631 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 54538de8-564b-3a35-a3d0-80073d557081 | -3.05413 | -54.2213 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1d91c26d-e1da-3442-86a0-43dbfc07b4c5 | -3.0467 | -54.21131 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d015044-67c2-3106-b992-298d260fd510 | -2.76902 | -54.09812 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d7e090ed-a23e-38f9-9485-525157393a3a | -3.26881 | -54.02507 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| de456547-8e4e-3970-89ed-396226503843 | -3.26846 | -50.40808 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 70bed235-079c-3c95-8c09-e0e6b8b1434f | -2.78438 | -51.66959 | 2026-10-07 07:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 550e9add-e623-3ff1-bb62-eb745d839e88 | -3.84935 | -55.99365 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe70115a-4220-31ce-97c6-d7ba43969864 | -3.61488 | -55.28496 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 04695f9d-ad75-391a-8cb4-dcc7ebd686fd | -3.52912 | -54.63113 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2baf5e12-f141-34af-afb0-9edcff65c946 | -3.04717 | -54.14913 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 710f8760-dc57-3628-bf95-45355b09e7aa | -3.38501 | -58.19608 | 2026-10-07 07:18:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8ddb088d-9d51-3b1d-baf8-65158816fabe | -3.2749 | -54.06736 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0fd76502-440d-3270-813f-93f41e34d2f4 | -3.07649 | -54.27484 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 748a7883-31cc-3473-b113-4bf5501f4c2d | -3.21849 | -53.88372 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 57f345e8-b150-32de-99a8-870d65b0f7e2 | -3.07169 | -54.24747 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 152a070a-0a8e-3d7a-b999-63e2b8ffd02d | -3.50015 | -51.69409 | 2026-10-07 07:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5a9f3d84-e59d-39d1-9ed0-97b522970142 | -3.09304 | -53.72732 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 91ce08ce-9497-3daa-8246-e8f44e364976 | -3.1375 | -51.02569 | 2026-10-07 07:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 672eadc6-6725-33d0-9417-c672cfc49514 | -3.1712 | -50.43997 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 49d029c2-3760-3a47-9d3d-0097f1627776 | -3.01349 | -54.13528 | 2026-10-07 07:18:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aec17869-81af-310a-8c93-dc6d644d3657 | -3.28892 | -54.03377 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 363117e2-2558-3b38-a160-61864d6e86a9 | -2.77033 | -54.08943 | 2026-10-07 07:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 58bc17e8-dc63-3d0f-b7fa-3b249b612a7d | -3.29373 | -54.06122 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 52e424f1-bbff-3f67-976f-3b8f04b17a0b | -4.15463 | -55.14897 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 36f04d0b-304d-32f4-976f-bfd81408ab43 | -3.17559 | -50.55595 | 2026-10-07 07:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 1de60aa9-721a-3076-b899-445fa97a075a | -2.94995 | -54.06594 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 0b2e261d-cbfd-3ac2-af19-73c894fedf78 | -3.07037 | -54.25616 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b0a12c58-d7dd-3c3d-af71-77967ac40ec9 | -3.11143 | -53.78383 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 440e4808-7eea-3cf6-9d0c-2eecbe19f225 | -3.08175 | -54.24006 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6a0385f5-7555-31b9-acba-3a3f39ffba36 | -3.2876 | -54.04249 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c5417e08-224a-33fb-85be-2c798f34d561 | -3.61622 | -55.27608 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 4ed4f09c-595f-3250-bf59-9d881c68df52 | -3.53523 | -54.64985 | 2026-10-07 07:18:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5bf600ef-2c27-3ead-9560-8af3f42174cb | -3.0778 | -54.26615 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3d414cab-f465-3ab5-96c4-1beb10da52af | -3.27013 | -54.01635 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b48016f1-9689-3a9a-99fb-070eba650d2c | -3.12472 | -53.69603 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d9861d69-6638-3e87-bd40-bc95ca4bc969 | -3.2911 | -54.07865 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 47ea561e-22c5-3617-8f04-82fc76b7c59e | -3.85221 | -55.97505 | 2026-10-07 07:18:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| be69189b-1d46-3adc-a46d-a18e803d0d96 | -4.14292 | -54.9166 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dacdeabb-a470-34df-9211-8b2ffbd6ef40 | -4.57165 | -54.95797 | 2026-10-07 07:18:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc5982b4-7793-3077-b42a-2d8a6a7eab8e | -3.08044 | -54.24876 | 2026-10-07 07:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 098a7dbe-7799-3692-891c-717fee9f47e8 | -3.27753 | -54.04993 | 2026-10-07 07:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 495749ba-6ce4-34a6-99cd-2e7249602b94 | -7.21417 | -55.16432 | 2026-10-07 07:20:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| be43c83a-d415-3320-878a-2746aa1729ee | -8.71237 | -45.18159 | 2026-10-07 07:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c8f08305-095f-3d2a-88fc-64c598fc870d | -5.95572 | -55.35293 | 2026-10-07 07:20:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50e30220-9081-355e-9382-a03f6c1f6cc1 | -6.44765 | -55.02158 | 2026-10-07 07:20:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fef36496-370d-3405-a481-80590e31903a | -8.50574 | -54.62364 | 2026-10-07 07:20:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a72ed2ea-9dad-3bc9-8c06-fdbdbf4c5a1b | -5.95705 | -55.34418 | 2026-10-07 07:20:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56920c9f-9045-391f-ac19-0bc1d5e59368 | -8.71484 | -45.18641 | 2026-10-07 07:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3c31911e-bc1c-3e04-8993-4aa01121688c | -7.21284 | -55.17308 | 2026-10-07 07:20:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b324e754-20cb-3aa1-bfb2-0608b6b8c9bc | -8.9046 | -49.97714 | 2026-10-07 07:20:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |


[Clique aqui para ver as próximas entradas](README125.md)
