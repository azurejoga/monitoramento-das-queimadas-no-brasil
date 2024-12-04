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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3be200c1-b2bb-3211-8fdf-84bb7c7ddea1 | -1.25587 | -54.53743 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8a91f03-47e2-3c3a-9126-cc018d28702f | -2.87703 | -54.04186 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e2acab73-16b5-3af0-9bc6-22a22411058b | -2.82652 | -53.05508 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a6a26529-12c9-34ba-920c-53e9fb180a04 | -2.77707 | -55.31702 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89ebb2af-22a5-36ca-8652-ac0f8c722621 | -1.11666 | -53.81425 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c68f75e6-3259-384f-b24b-8bc73264a203 | -2.07299 | -45.48439 | 2024-12-04 05:03:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b38cef10-ee81-354d-b798-bb044a6d5adf | -2.81277 | -53.02982 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54548997-27e1-3de6-adc8-a7791cd1a81e | -2.69205 | -51.86567 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff777694-7367-3005-842b-1eeba866ed0c | -3.85743 | -52.15921 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dd05d2ab-48ba-3db1-acb3-bf84a03bb4ac | -2.77287 | -55.36559 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f5b184-2b01-3a80-86f9-0d86344ac258 | -4.37649 | -43.36435 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea7855e9-3e77-3d00-b4b3-17559fc72fc3 | -3.27305 | -53.63677 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94762633-1691-3784-9e79-b16da84d580a | -2.78001 | -55.36317 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89183733-d560-36ab-8576-f53647d93e52 | -2.43926 | -54.01418 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b414b9-1a0f-32d5-8a30-0fe208ccd467 | -3.26605 | -53.34228 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a738ff04-5f7c-36cf-aff0-372306cb5c24 | -1.67767 | -53.94693 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69f91f3d-a220-34af-9b4a-44fd8b25958c | -3.11355 | -54.0525 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edb6cafd-2128-3bb9-8bdf-3e040ee6febf | -1.62467 | -53.89576 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97382612-9ad5-3701-baa6-8f1027a713b0 | -1.93174 | -53.44398 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd412d85-bdb7-3d81-a63e-ca6a7de42ca2 | -3.48099 | -50.24125 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84852fd-3473-3453-afa2-d3155e1d9c57 | -2.89741 | -54.45719 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16673c42-2fb9-3aa1-b4c6-5fda52bff40a | -3.48659 | -50.93848 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13753e4b-4618-3ce5-aff3-bfd7f7957c18 | -3.32574 | -50.22194 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 610c9e43-0507-3ce7-a2fa-4137eb424e59 | -1.64013 | -53.85841 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97bc0c5d-9272-3eb0-b639-6f83f6891f78 | -1.70505 | -52.77224 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4144d2d9-3044-39cc-92ff-0d663d5e6de6 | -3.20137 | -50.65148 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29401207-f84f-3edd-a25a-bf56ca56f4b1 | -1.40204 | -54.99606 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df83af4-6a92-3e04-a172-76a3f9eec170 | -2.80412 | -53.04006 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca2fc80a-e500-300e-9dff-5b0976d86e33 | -3.92499 | -52.39579 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b4857c2-b55e-3c22-8383-8f0515d58258 | -3.34511 | -49.76839 | 2024-12-04 05:03:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 977ccccf-c1d4-3028-bc14-18fadc5139d2 | -3.37749 | -51.05945 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 738d7088-67d0-3f66-8cca-af906fa8fbd0 | -2.77314 | -54.11989 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5faf54c2-92de-331c-bbb5-89eab6887016 | -3.02935 | -54.06491 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2986eb1-6a2a-349d-88ac-a85ed03b0e98 | -3.25334 | -51.14015 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 881508e6-68f1-394f-bc59-7130a4c8511c | -4.01757 | -49.96545 | 2024-12-04 05:03:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d12d9925-15aa-3118-972a-fc664e012384 | -2.56636 | -54.35592 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0484f89-d699-3ca6-901b-e81d8d63fb0a | -2.57183 | -54.34262 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ac5ae07-b663-3df6-9d6e-6464ca5e7537 | -3.13515 | -53.28124 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3db1239-fd05-3d80-ad37-da283cc38169 | -4.111 | -50.98059 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664f435f-51ee-33fa-a790-103a54291780 | -2.97791 | -46.95142 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3611e01b-5a09-33e8-9955-5a36ef77bbf2 | -1.49682 | -51.9502 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e5461f9-0353-3932-8bf1-ec2358f06372 | -3.11771 | -53.09821 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef74c0fd-7821-3eef-9e05-cd019f1195aa | -2.57149 | -54.80265 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64b1f8ef-17f7-3d3d-b999-fe27ecce7382 | -4.01813 | -49.96164 | 2024-12-04 05:03:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 944a6a97-d168-3239-8a45-186c439939a4 | -2.87533 | -54.03074 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebce0fa8-7d1a-3d0d-8d5d-634f8fab287e | -2.8018 | -53.05513 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b6f19b-b133-396a-a92e-7ea7db33d5b0 | -3.31983 | -50.34386 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7150a29f-c13f-3f9f-9c12-c68e773fc487 | -1.65422 | -52.39228 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 195d6558-8f4c-3533-9c83-a028691345e0 | -3.70809 | -50.45214 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18f47150-6614-3b80-9382-3400a02633ec | -2.34743 | -54.38626 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fcb85bdf-7476-356c-90d4-c8442a5b5e27 | -3.2424 | -54.09403 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d739ff52-4ce9-37c2-9377-d80f8b81984b | -1.65481 | -52.38838 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51436e68-c350-3088-964f-d7481d92c735 | -2.20098 | -53.7709 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd43e532-e166-38e2-a46f-283b748ad81c | -3.4869 | -53.8171 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c34f82b9-b6f8-3f44-8687-4f242c720249 | -3.03202 | -54.18084 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73527ab1-f34b-373f-a207-0f62bd58c168 | -1.68485 | -52.79314 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3248d6ca-17d8-34f6-b0a5-0c0773592a2d | -4.74178 | -45.7011 | 2024-12-04 05:03:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbc9c53d-f5f4-3a98-98cf-f513ece38373 | 1.08413 | -55.99077 | 2024-12-04 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbf6ecc3-c397-3e7f-8cf7-d6730f079793 | -3.55708 | -50.17859 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 890cc05b-24df-32d3-9a06-735831f3f68a | -3.10296 | -54.05447 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80ad8aca-4f8b-3092-9ea2-8477f89e0c23 | -2.82668 | -54.14592 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4eef2b5f-3fbe-3246-9054-f69640e8d3d5 | -3.28944 | -53.70985 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0053ccb8-251a-3864-8ba9-fd10f6b3eec2 | -1.62079 | -53.89874 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 863638ff-f973-33f1-ae0d-ecc05462dc57 | -1.46183 | -54.95962 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89476635-f1e2-3e13-8317-5b30771e5cfb | -2.80164 | -52.37275 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c96ec1-7951-32ef-a01c-0489cc24997a | -3.11758 | -54.61591 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39c89dd6-b802-3397-b603-8845ca2b3635 | -4.0151 | -49.95336 | 2024-12-04 05:03:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb28fc81-6eec-315a-a416-0a9859ea175e | -3.29341 | -53.66213 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a8cfb70-a8bd-386a-b2aa-99f896a121ad | -1.2387 | -51.60172 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8df1cd93-a57b-3e36-8c48-e936a62ef3da | -1.49113 | -52.52696 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf731ddf-e193-38bb-9243-aa4c443b02ae | -2.58711 | -53.67296 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5a386ed-a990-3100-a88a-2de35e12cd91 | -2.6063 | -54.23011 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1adccfde-101a-3fec-8c5c-5e9aa419cfd3 | -2.52432 | -54.0344 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e5e4e5-b5d4-3cc0-a2a5-ec589c920bb3 | -2.87418 | -54.01608 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 590d2455-6e42-3413-981e-10de759555aa | -3.14103 | -54.53074 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cb61c3e-3729-303b-b96c-b379906b3797 | -3.1566 | -51.11383 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d898163b-ee4e-34d3-bda9-84ac71535da1 | -2.90599 | -54.24778 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 732fe403-039d-34fa-ac58-d09d394b4c14 | -2.41758 | -54.02164 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f01859a4-6b89-3466-8b61-2df6fd1ee516 | -3.24817 | -53.61803 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62e8e9e2-b0ec-320a-95f1-f09970e9c540 | -1.40534 | -54.99657 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dc718d1-d734-3bb6-bac5-35d648c105b2 | -3.08089 | -53.38272 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70cbc99f-0d39-348f-a947-3248ce0d9810 | -2.82433 | -51.83529 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf58df74-b9e2-3bea-b291-bcd035b2a03a | -3.8002 | -51.99117 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77fccad6-62a9-310a-b430-7c33cc0bd387 | -1.55596 | -53.78783 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39165191-982f-36b0-ba1b-c17e4679d120 | -2.58373 | -53.67245 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f094fcd-35ad-36d2-acca-2c5484eed1f7 | -1.553 | -52.01277 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af928378-fc43-3916-98d9-536e37ee982a | -2.4321 | -54.03828 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92ffd07b-7106-33fa-a784-c36ae018dbd3 | -3.29928 | -53.67745 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e8e7968-fc28-36bb-adf5-9e5af82279d6 | -3.52453 | -50.47765 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfa9d32d-b480-3f49-b34f-526f3ac1a20c | -1.43238 | -54.51961 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920c4c43-a269-3a58-be7a-faf99604c45b | -3.42462 | -50.17386 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cae929a6-edbb-30d6-a591-a42e2d606cad | -3.26404 | -50.21568 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 639e0d11-e15a-340a-9c2a-e2f9b1ce2eda | -2.46398 | -53.63224 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57755253-4bda-3221-a48b-5aad0adcab08 | -2.8648 | -54.05444 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 255eb7b2-7fd4-3b5d-8b55-01b99b4ce807 | -2.20405 | -47.2502 | 2024-12-04 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02188ac6-0b90-32a1-bf66-ec2ca31e68e5 | -2.25666 | -51.25352 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c68c431a-1773-3979-89c8-14ac9000a2a4 | -3.26004 | -53.63111 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02c0c9a5-8144-3181-98bd-07f95c83fa5d | -2.44212 | -54.03982 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ea98f15-57f3-3635-ba47-47a684f32d52 | -2.83705 | -46.75577 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 232c8fdb-e85f-3977-9af2-a06a025ff5ba | -2.90563 | -51.81706 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README33.md)
