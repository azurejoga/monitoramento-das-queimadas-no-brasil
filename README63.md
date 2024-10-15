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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11167595-e2a1-3a8c-942c-4ba9cba34fde | -3.8021 | -51.94416 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6335e54d-b515-3f5e-8488-ec1b8800b835 | -3.10259 | -53.03825 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e43c6513-8adc-3942-8fd6-9813cb8c8cea | -3.79724 | -51.97509 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79208346-d55c-3ac5-9bd0-384571765570 | -3.77602 | -51.70062 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5eaf081-da4b-36a3-9853-05c36915fb22 | -3.75256 | -51.93645 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a10ec873-43a8-3492-b4a0-b6eff3e917bf | -3.74926 | -51.93594 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a29d8d36-7384-3072-81c0-32f615674ba8 | -3.71645 | -51.79664 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 289cab34-4e7a-35a0-8365-6da5f811ad77 | -3.71369 | -51.79269 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df351ada-9256-33cf-8b4c-17464447f7f7 | -3.71315 | -51.79613 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f297e18-8500-39eb-ad3c-34f834cd2005 | -3.71039 | -51.79218 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2640dbdb-b334-36ca-87d8-76f3955fa67c | -3.69926 | -51.75526 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8218c822-6d32-3d10-b05d-a55187496a08 | -3.64916 | -51.92348 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170143e6-7c30-3d00-8d66-7da869b0bf03 | -3.6433 | -51.80993 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5a7f7f19-b985-3566-9f8b-b4cccae69f15 | -3.64018 | -52.04525 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35cefc93-54af-3dac-90ba-2e041301cd56 | -3.64 | -51.80941 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 306bfaad-65fe-30e5-93ce-3a8bbcc72c79 | -3.6251 | -51.79653 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c3add6e-d6b8-363c-922c-bfabb8adc50e | -3.62468 | -52.01468 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 788bbb63-c3ad-33a3-bc30-ecb224e3131c | -3.62138 | -52.01417 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7140b5a-9971-37ae-8a9d-9d72d48618be | -3.61814 | -52.03478 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7274250e-90dc-3c30-8730-dcb382088a18 | -3.61484 | -52.03427 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffd90f0d-a34c-393a-ae15-cefb4e21c052 | -3.60165 | -51.79277 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e3e55b-870d-3456-b0e2-8983692c78ba | -3.55174 | -52.02431 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 678cf35f-c450-3de3-a26c-5876efdcc59e | -3.5512 | -52.02774 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56666519-4965-39a5-9def-44de1fd9974a | -3.54844 | -52.02379 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4e7699-0e7e-3712-bf67-fceb1e231db1 | -6.24425 | -52.72731 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820afca9-e7e3-36b2-8834-331ae924bb8a | -6.24371 | -52.73076 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b82da5-6972-35a7-9899-189b045d2f14 | -6.1051 | -52.70501 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65dd007d-003b-39e3-8796-94d79551c691 | -6.5126 | -51.43995 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd6ecd8c-9e9e-3ec4-99c9-a9350a490c1e | -6.51206 | -51.44349 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96618ad5-45e8-38fb-b134-623905bdfa48 | -6.50925 | -51.43944 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c1feeb-d0d0-377d-9657-9349d3e8442a | -6.50871 | -51.44298 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d9eb117-a03b-3b68-a3b1-a109790c2b37 | -6.50645 | -51.43537 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 111f5c74-91a6-38d5-89fc-a30a7d23c354 | -6.34525 | -51.7565 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32e9e16-7659-3e34-9b87-24d05e362c59 | -6.3447 | -51.76 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ef1b8a1-b223-3a60-abd4-3277d4198786 | -5.82596 | -51.64384 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 13cdcabf-8ef5-3413-a3b0-c5107c85978b | -5.51747 | -51.1163 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 396b1a4f-6102-38a7-a598-b0f88ab30dc9 | -5.51411 | -51.11579 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef6af229-5cea-39b1-92ea-fd49a921d9ec | -9.34122 | -52.84105 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d91ee9be-b283-32f4-9c3c-9b176ecc905d | -9.33297 | -52.85046 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e1054ed-3eeb-34f5-b0ef-ecc5c25a972f | -9.33243 | -52.85394 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 075039df-08f6-38ba-872a-f41b147de156 | -9.05384 | -53.00628 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e57df95-e902-3eb9-9a39-d385d13bbec4 | -9.05054 | -53.00576 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cd2be06-d3ca-3148-8bbd-450cdba7fc06 | -9.04669 | -53.00871 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a7ac1f3-5136-3f57-82c7-2b93bce9273b | -9.04338 | -53.00819 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e9debd6-8174-3531-bed1-51ef6650d6fd | -9.04062 | -53.0042 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 893fe4c5-8b05-3c17-9185-ec5f239b160f | -9.03615 | -52.96784 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f121270-9261-3ce2-b68b-f573b47a7498 | -8.85292 | -53.03105 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41a388da-df3e-3249-a29c-260818975797 | -8.85125 | -53.0201 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f6942c-02e5-3707-9c0f-81e41493b852 | -8.8507 | -53.02358 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eb61cfa-6686-3064-bdb8-719419a3cd73 | -9.88284 | -52.27964 | 2024-10-15 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7690273-83fe-3c3e-bf04-9e88ac7aba25 | -10.20269 | -52.31871 | 2024-10-15 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac06870-08f4-32bd-bb3d-a02ebd43b7c7 | -10.20215 | -52.3223 | 2024-10-15 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a06ce2ec-104f-33cc-920c-f70c06af263f | -10.1988 | -52.32178 | 2024-10-15 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf30b00-b5dd-3f03-809d-64b9ce57456d | -10.10283 | -52.61593 | 2024-10-15 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 783ebfcb-3bd3-3d4a-b2ee-e3c28dea2fd9 | 3.31939 | -51.31514 | 2024-10-15 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97767429-e517-39e4-99d2-1cf4e7a30c2f | 3.31884 | -51.31165 | 2024-10-15 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 574290a8-3e25-3a69-94dd-1b9dda84f4e2 | 2.40079 | -51.67548 | 2024-10-15 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97f3f53c-2093-3d4a-bc58-f28dc1ae30b4 | -3.5369 | -53.51958 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e6279e7-9597-3f50-9e79-d7a90dc99543 | -3.32661 | -53.38686 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b1e111-7ca1-3159-af29-f69d217d0a83 | -3.14378 | -53.16813 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28f6f925-84ef-324f-ac5f-ec0a5c1f439b | -3.10315 | -53.03473 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f574906f-466f-3fc8-9d7f-d120a84d9070 | -3.10203 | -53.04178 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a24fd9-a919-37f8-93bf-8592d9a3f850 | -3.1009 | -53.04884 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c20819b-99a9-315f-88f6-4371999b213c | -3.10073 | -53.03411 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 998a3fac-fab3-3188-bd46-46b1ddee3e9b | -3.10034 | -53.05239 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb82e9e-8259-3c1c-9f4e-a17f885f89cc | -3.10018 | -53.03764 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12879f5d-e1f0-3bb5-aed4-c666e74a884f | -3.09962 | -53.04116 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e508f9-059c-3004-8712-971d8ab5369d | -3.09907 | -53.0447 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a352a2a5-dc85-3754-9ddd-4b05d860a19f | -3.09851 | -53.04824 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667827af-e04a-3d29-abf5-70e2cff432ad | -3.09796 | -53.05178 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0154eb75-5313-3c7c-a13e-10fd0e565684 | -3.09739 | -53.03358 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50ab3275-9a64-381e-b42c-d8fad496e657 | -3.09683 | -53.03712 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44508fbf-4bc7-3ab6-87b3-c24eb4eb8ec6 | -3.09628 | -53.04065 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a387270-3a79-301d-a6d1-4feaf736c84d | -3.09572 | -53.04419 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f65604b9-dfee-3e22-a4e2-c2bcf4bc4754 | -3.09348 | -53.0366 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b70ff85-303d-3dc4-b33b-5f31a757de23 | -3.09293 | -53.04013 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 362d7662-52a8-3c17-807f-a6967f4294da | -3.09014 | -53.03608 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d57c8a8-56f3-3e77-ae54-12b8af985fa5 | -3.08958 | -53.03962 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89a730a8-cf2d-301d-a3f9-6d73ad2e607e | -3.08623 | -53.0391 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ef69b42-07f0-311b-84c1-7ab1d41c7f43 | -3.07844 | -53.06681 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1190918-1495-3f17-b045-a62a700b9320 | -3.05213 | -53.25596 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6682b95-f3d3-3d07-974a-97558ff47642 | -3.05156 | -53.25956 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1dff4c3-1242-3c16-bee3-84c386ec03aa | -3.051 | -53.26315 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47f98ee8-dc3d-32fc-8c07-b5058093a460 | -3.04988 | -53.24831 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6228f0d2-307c-3c0b-856d-bea5234e8eab | -3.04932 | -53.25187 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 391abc12-8e3d-3c46-8d07-954e0c55e50d | -3.04876 | -53.25544 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cac4e87a-d88f-35de-b8aa-216741af2549 | -3.04819 | -53.25904 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a8ed2d2-5192-3cd5-92a8-3e8549f202d8 | -3.04763 | -53.26264 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 634662a9-6440-3b93-84fd-2ca6a19e3102 | -3.04708 | -53.24422 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b23a3ac-c038-359b-bea5-75e10695e542 | -3.04652 | -53.24778 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af059ea6-c590-3943-a187-744d72d20dc9 | -3.04596 | -53.25134 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 856f2a05-b541-3734-a9c2-9ce9de96000a | -3.04539 | -53.25492 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19424aa2-61fa-3f6b-b337-8fc9bd9e8db1 | -3.04483 | -53.25852 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cafb89d-3813-3a86-accd-4e96d56d2c72 | -3.04426 | -53.26212 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a7a4ad2-30d2-340b-992e-ccc0e9342661 | -3.04385 | -53.04685 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f1f2e1-89d3-32a8-8e90-fb152d77a01e | -3.04315 | -53.24726 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 089192ba-0af0-367b-8e35-a2a0944a20fb | -3.04259 | -53.25082 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79c0ce60-3363-30cb-8a71-02d4ff8b0aff | -3.04203 | -53.2544 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27328873-4543-36f3-94d1-fc5ab50291b3 | -3.04146 | -53.25799 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1615785b-1abe-381b-95ee-f8adf416005d | -3.0405 | -53.04631 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
