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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6d05843-4aa9-35a2-aeb7-e933ad13e13d | -2.14841 | -46.48697 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8c1ca22-17f3-3a2b-aeb4-be589e4145ae | -3.54814 | -45.81133 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da7cadf3-2069-3711-8d29-8de341c9c6fa | -3.43926 | -50.12508 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec80ed78-015c-30b7-a1eb-1bc3f1d6b650 | -3.06035 | -51.05755 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8520e40a-f51e-3a81-8219-94a960584d37 | -2.65913 | -48.78646 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaa7d210-787b-3d58-99f1-4cc2ccf43889 | -1.57782 | -52.26821 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0510328f-a47c-3198-ad46-550e2cc909a8 | -2.43055 | -53.66083 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a31cd1-4220-30f3-89c6-0cb7f6aa9ccc | -2.62953 | -48.32066 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28441a9f-a0d5-30f4-8bb8-704cd80df7d9 | -2.13443 | -45.33207 | 2024-11-30 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9711f026-a651-34c5-bff8-382951158fc3 | -2.55258 | -47.30218 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc9a71ac-0c8d-3ff8-ace2-0f4f23160d00 | -2.33108 | -50.67535 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4d42ab7-64d5-3a56-aad7-0ebdbcf43f15 | -3.18737 | -54.32629 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deabdd98-1d0a-3eda-a812-fbd996aed16e | -3.30359 | -50.49336 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcbf6fa8-b4c0-33af-a53a-20bc9d6b057b | -3.24505 | -53.6251 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 481d35b0-b5fa-3db4-9946-6e149e4b24b2 | -2.61467 | -54.07391 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 546edc3c-5953-3e45-96c2-845bd6a2b8bc | -3.89765 | -46.65414 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c955d50-b2bd-358e-861d-cc6edd9e4b34 | -1.59265 | -52.2705 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82948055-9fd6-3d86-828a-4a5d04238eea | -1.91531 | -52.90651 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f6ff305-6c8d-3bc2-bc1f-04f99dfac60b | -3.0938 | -54.13166 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4895aa7-e559-3cf8-985f-89c8be6e0459 | -3.48037 | -50.25069 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b61719ef-4247-3b73-8cff-ad05fe9b45cb | -3.55629 | -53.54032 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8c2445-1de0-3dd3-9157-dd27e996ec3a | -6.38088 | -44.75995 | 2024-11-30 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3814c5ff-e716-360e-af26-21a8b28e79be | -1.14447 | -53.66256 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ff6c9bc-902e-3e48-93a3-60d8a921d11e | -3.6977 | -47.13132 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aeba07e-bbf8-3469-97af-175c767c8e80 | -4.06654 | -46.69062 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e0fec6e-b6be-3691-97df-186978dcbc77 | -4.15038 | -48.99526 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26d376b3-4c97-36c7-b2d4-6f3c672f3ff7 | -3.98638 | -49.93439 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd5a5bab-ee62-3266-93e0-116a6648aea1 | -2.62805 | -46.19496 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83811198-fdbf-3d18-860d-d512822b8928 | -2.85428 | -48.09986 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8194efc-64d5-3120-a36d-819fee233af8 | -4.11703 | -48.53085 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76d91aac-2561-37e8-bf81-7057058180c2 | -3.77533 | -46.6958 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9489aa75-af6d-3d21-af1e-44dbd7111252 | -3.67612 | -52.11156 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6aa38e8-eaba-3718-b93e-f19e4228af10 | -2.00948 | -51.18343 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 438d8944-6742-3605-8976-1f213a8e2fb9 | -7.86134 | -45.92408 | 2024-11-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f160e96-cd10-39c4-8e6d-e642f7ee8153 | -2.9528 | -51.07208 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6345de86-7eec-3fb1-9d6d-038d7da75fee | -3.30072 | -50.76083 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2968cc4-6e6c-35c1-8af6-4855e4100f10 | -3.13862 | -46.61765 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8626430c-3982-3e99-8f66-ff99712cd879 | -2.86793 | -46.82519 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9444873-9608-3b58-900e-e2b74622ee2d | -6.89821 | -43.54136 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 280864e0-86cd-3250-b564-4dce9437d35b | -2.68236 | -46.14679 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81264ae5-8668-366d-8940-a0564bcb10ad | -3.83182 | -46.56153 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32bb79a9-2b82-3957-b753-b2f161ee714b | -3.28441 | -54.16594 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed1e0b0-fab5-3729-890c-f512676f2496 | -1.1487 | -51.6835 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58586dfa-9873-35b8-9c23-d928780a24df | -2.80363 | -54.06667 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0573b07-70fa-36ad-bb2c-d3596dd0998f | -2.7598 | -49.40486 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73e2a76f-e967-305d-b9a6-79bb4b217b99 | -1.42195 | -55.27246 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 630561bc-dc4c-3947-bc14-de8bf9fdc6a4 | -2.69316 | -51.99715 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d380820-f11b-3df3-a908-654e324395e4 | -1.97256 | -48.43303 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4addc66-a0ff-3bf8-8ace-6a54abf08c5a | -2.76158 | -54.11952 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70d15687-8028-3ad5-915b-d93497a2da56 | -3.15995 | -50.5822 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8009b9f3-2bf5-39c8-bb64-8af35d438e6d | -3.14713 | -53.83024 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 08a74ca7-3d0c-3d57-bc4e-5192355419f2 | -1.83083 | -54.52892 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 79fd98b3-a320-3de6-aa91-4a375bc33172 | -4.1038 | -46.11482 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f954a8c5-ca4a-352f-9784-d821f6dd332f | -3.09862 | -54.02611 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c06d46bd-16e4-3451-890e-dcdfec5cb2c4 | -2.30099 | -50.68623 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f3d43a1-4673-3adf-8f30-63f64a29a8bc | -0.82112 | -51.59781 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07572b14-6969-3c30-a04d-be02fbb323b6 | -3.69064 | -50.08483 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4241b00-9cb7-32e0-9626-d86088346b4a | -3.36097 | -49.75769 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d8b9d4db-bc28-3cdc-9ec4-aeaf3fbfc995 | -2.29357 | -50.68887 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb8f6b04-1437-3ba2-b365-cc3d88ae7a75 | -1.26662 | -47.87801 | 2024-11-30 04:40:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f12fdad8-74cf-3390-aeb1-22a1326cc3f9 | -3.1107 | -53.76186 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b63dbde8-cb2b-3a2c-9da6-712aae920a00 | -7.86581 | -45.91996 | 2024-11-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65f70e54-f6fe-3ade-a7d9-d2cde1933e2d | -2.11674 | -50.33938 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3315ab5c-7074-3819-92cc-7413ecdae3e9 | -3.90053 | -46.65857 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b29738b0-dfda-367a-9d6c-0eac368f8c58 | -3.93624 | -46.71527 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d154b3bf-7146-37cc-9dd0-92e3fb8ebdc7 | -2.61844 | -54.20959 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e153651b-ae2d-3eab-8f93-4419de7ee4ff | -2.69759 | -48.64825 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8626303-2a2b-3913-bce5-bab3683cbd34 | -2.6399 | -49.90965 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 189c1d6f-9f74-3bd1-9c19-aa61cca1bc10 | -3.98298 | -43.38949 | 2024-11-30 04:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 230b1f32-014b-3eba-b4d1-8e8f7036c405 | -2.80304 | -45.71202 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e2486b-d17e-3779-8d9a-f62cd3c12ba0 | -2.4475 | -53.9703 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 486708cc-92fe-3b98-b6ce-89442e546b56 | -2.73703 | -47.53908 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5dd427a-c9e0-38f9-9e62-4082a7e7713f | -1.53553 | -52.65887 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9d19d4b-594a-35b0-85e3-f0bbc64663d1 | -3.08508 | -49.21534 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c7c6ea5-2032-3842-85ca-290e50045c0d | -2.69171 | -46.1563 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1259190-ea61-396b-adb6-f895b9e16277 | -1.50499 | -54.95071 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a7396858-32a4-3d18-a849-42a7c39f6421 | -2.36494 | -50.4185 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c83b8c-e27a-3ce9-8bec-ef50d375c3a1 | -2.36264 | -50.43299 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e861917d-34f9-3fc0-b29e-f969080158d6 | -2.89145 | -54.16946 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3220d6c-23ba-30ba-b979-246cb43c6919 | -3.27799 | -50.15367 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee01edf7-e879-379b-bc1e-431333319528 | -3.70169 | -47.12816 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fd96b22-3964-3c7d-8811-06649124613f | -2.18416 | -47.13935 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8c83f04-6469-34a6-be11-ec54a104f5f4 | -3.15898 | -49.02695 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9542cee3-a0d5-3475-b783-9074cf61e6f4 | -2.69795 | -48.60258 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb72a8b-e4e4-3534-b1cb-7af34640c847 | -4.40415 | -47.25938 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58c3590e-22b9-3a70-a4d8-e4ebee9d99a1 | -3.59711 | -50.3742 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d578baf-0e35-33be-9cda-51e6f7af0e77 | -3.69946 | -51.80557 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0801d7-193b-310b-adaf-6d06bd6d4b5d | -3.90629 | -46.528 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 272e4921-cd94-3d59-985e-0a1f39f1cf92 | -0.88226 | -53.68425 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 872871d1-aab6-37fa-b179-f4b6490dba9f | -1.33007 | -51.42467 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c325404-6181-3b9a-ba8e-64b5ba22bf08 | -1.31709 | -51.7367 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5cfa15-9bce-34f9-9deb-f4814822975e | -4.04546 | -46.85255 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e45f82a8-f85f-3c3a-933d-d903feac03e3 | -2.82215 | -46.84869 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 413cc9da-145e-3b09-a6ff-8cdf9665cb4c | -1.83606 | -46.30437 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd73bdfa-6586-360e-987d-e7809ec27764 | -3.3416 | -50.52552 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aafa8d24-399e-3068-887f-0f329cf66dc4 | -2.29299 | -50.69257 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de377ee5-6cb6-327b-9dba-efc1107a6559 | -3.28077 | -50.15773 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38a802a6-282e-304e-801a-ea52fcec895a | -3.04689 | -48.52325 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f955f6b-c9cd-37b5-a3b3-cba1dc90f369 | -6.91192 | -43.53914 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f4a09c5c-1efc-3b02-90dc-b0214abe416f | -1.67201 | -52.40872 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README69.md)
