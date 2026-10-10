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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c0d4bb-6a86-3495-a228-f780f3ca95c3 | -8.421 | -70.12527 | 2026-10-10 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b60cc9c-d6ae-3e09-a693-27bf2c86d492 | -7.70115 | -73.10169 | 2026-10-10 06:46:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f6e8818-ec3f-3455-9357-8f45663d0041 | -7.70048 | -73.10635 | 2026-10-10 06:46:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e065459-7b01-3571-9183-53dd3187ac3c | 0.00166 | -60.57978 | 2026-10-10 07:33:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0f0b87c1-2f5e-3144-9b58-a78b5cc3144e | -4.40671 | -49.78446 | 2026-10-10 07:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 6c41206a-b7f4-3d77-bcc6-b773393b497a | -3.53723 | -54.7451 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2fab57bf-f014-3c43-bb82-5ffddf54aa14 | -1.88595 | -54.67266 | 2026-10-10 07:33:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b5c32f65-063c-3e16-b8ee-9d7a14286136 | -3.59024 | -54.59375 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f5ed9732-fc6a-3316-acf6-be0b66939a29 | -2.38689 | -57.8974 | 2026-10-10 07:33:00 | AQUA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6986aa28-61a6-369f-9c47-37818e3566bf | -3.3061 | -54.01202 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 75ee0cfc-50e9-341c-9636-d4dc9d638ab9 | 0.01151 | -60.57833 | 2026-10-10 07:33:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06fc73d5-a186-3325-b254-99167875d358 | -2.999 | -53.88903 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fed108c5-8b6d-31d0-b99a-9bbba6aa931b | -3.60225 | -54.58303 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dff5603e-7e24-3604-a29d-dcb2a18542e3 | -2.49117 | -58.07621 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9c4cecdc-8e9a-3b55-b505-56ae1aa49317 | -2.74999 | -54.10685 | 2026-10-10 07:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ea9f14c8-1e61-3d30-a212-2245a7ce1c1a | -2.55155 | -58.03179 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ab2fefa4-cac8-3125-ba51-8e65bc213bf3 | -3.20331 | -53.85498 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9c0c51f8-ec27-3b2e-9c79-b3963286f42d | -3.10785 | -53.77386 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 12d435d9-5d77-3c1d-8955-f8386c6fa48c | -3.22508 | -54.29672 | 2026-10-10 07:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 88092fc9-e3a8-3033-b302-563887394169 | -2.80197 | -58.26554 | 2026-10-10 07:33:00 | AQUA_M-M | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2ce0a3b9-34e0-3d0b-9a95-daef3426eca7 | -2.44998 | -58.02884 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7f42cdd7-96d3-345e-8d97-5a04c315a74c | 2.725 | -60.26294 | 2026-10-10 07:33:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| f6628765-8bfd-3dd9-b09d-cdf9f67bda3e | -2.92765 | -54.07938 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8692374e-dde4-3994-8ad9-fc740f4627ea | -3.13045 | -54.17311 | 2026-10-10 07:33:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9d35a11f-51bd-37e6-9dbe-711d40eaa91d | -2.41894 | -57.99762 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe1ef44d-2d74-301b-bdc2-f845eab30e63 | -3.1905 | -58.63916 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b63f6b55-4606-3e8f-aff1-16494b70d162 | -2.93816 | -54.08091 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6d1ebc07-852a-3d8d-ab77-36a7808f7a56 | -3.12187 | -54.15873 | 2026-10-10 07:33:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d845aba5-a7cd-376d-a312-e8916be0b34a | -3.16684 | -58.61776 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7859ea04-5a78-3fab-b96c-eb42a5ba7cab | -2.73395 | -54.14347 | 2026-10-10 07:33:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 30876e6b-18bb-3cff-bf05-de4ce5b248fc | -2.39563 | -57.89869 | 2026-10-10 07:33:00 | AQUA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61ada2da-ccc0-308c-8442-e65c233707bb | -2.49992 | -58.0775 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 52a8ff19-a8d2-33df-8e70-65ef26dbd048 | -1.63955 | -54.40687 | 2026-10-10 07:33:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| faa54576-11db-39cd-8df1-8af022fd5492 | -1.27649 | -55.75119 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6d0d090b-e1ee-3be9-b816-82e8c8ff35e6 | -3.31221 | -54.67051 | 2026-10-10 07:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cbfa0c75-2676-33c4-9471-de3ad092c864 | -3.11662 | -53.78899 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 112b5304-03b7-38ef-9427-cb72d8d3c7e6 | -1.27793 | -55.74149 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba0ef3ba-1a3c-3163-9f19-317dc83dd2f5 | -2.84792 | -59.12233 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e55b169-6fd2-3ab2-b22c-dcf755c5ea7b | -3.03588 | -59.16258 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1f32bdf-8faf-3ccd-9213-20020370dcdd | -1.88852 | -54.66724 | 2026-10-10 07:33:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9326b59a-f966-3cf2-b704-37b250a2b6a2 | -3.19855 | -53.86122 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 74308c63-89e5-3543-a468-d36160495860 | -3.25372 | -50.4223 | 2026-10-10 07:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| fa367f78-757d-3eec-812c-fccaa7e1a53a | -3.22698 | -54.28403 | 2026-10-10 07:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f8d90466-4e67-3e56-aae1-324e1b01c081 | -4.41074 | -49.75423 | 2026-10-10 07:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| a9f9d862-37ed-3709-aa10-217819f054b7 | -2.8916 | -59.20808 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5bba016-4867-3a32-afe8-e8701337e4e7 | 2.72324 | -60.25126 | 2026-10-10 07:33:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2a5d05d5-4b81-33ff-9748-6bfeaa14b0c0 | 2.73503 | -60.26146 | 2026-10-10 07:33:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 96fbeed5-937d-3640-b715-f6a2f54e548b | -3.49496 | -54.61127 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4c16b768-1dfa-3ddc-886c-23a9fcef5de5 | -3.27851 | -53.8663 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| d14321b7-0093-3334-a7b2-28e411f2b7ef | 1.72785 | -55.56996 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7bc65f92-01c5-3bb9-9ea3-5cb5338b3957 | -2.45355 | -57.88721 | 2026-10-10 07:33:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dbd67c60-cbcb-3864-87a5-baf2b33bcaa4 | -0.98071 | -52.43953 | 2026-10-10 07:33:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| af843328-da22-3f4b-a902-bff48542130a | -3.56606 | -54.6886 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 04cdad18-fc32-3f09-a932-18f638dcdaa4 | -3.27841 | -54.68982 | 2026-10-10 07:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6ab81915-d662-3def-be73-63465f094c04 | -2.93141 | -54.05357 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 269e2636-f264-3dba-9276-87de9b0ebdf3 | 1.67147 | -55.6227 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0756ee81-9578-3626-ae13-2f83f9bdb404 | -3.25261 | -54.18443 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 440dec23-fd05-3708-a7e0-e6ef4bfba2fa | -7e-05 | -60.56852 | 2026-10-10 07:33:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 744462b2-2235-3f89-b109-ef29bcdbbd1a | -2.47068 | -56.05481 | 2026-10-10 07:33:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 47574937-5142-3c01-b3d2-ea51d244ea79 | -3.53819 | -54.73948 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 75d2f607-525e-3631-a5f6-ae37b8b5794c | 1.73686 | -55.56863 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f7433b8-3d3a-3d3a-a661-6a6008fc561f | -2.99702 | -53.90231 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| fab6279d-6401-393b-bef0-2eaefa9505c7 | -3.24415 | -54.02447 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e8cc1143-fe9d-39b7-8b40-03b8c7a30214 | -1.64132 | -54.39518 | 2026-10-10 07:33:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 336098d1-ae92-3cd3-a3c7-ba5f444ff5ec | -2.89024 | -54.06846 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7e2f61f0-4b7c-3816-a0a9-7c4565280082 | -2.49825 | -56.05885 | 2026-10-10 07:33:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 088f8c12-e811-3f14-9964-6227c553f4b8 | -3.02514 | -57.77706 | 2026-10-10 07:33:00 | AQUA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23027207-1c4a-3e89-ba2b-1b388a73b197 | -3.53893 | -54.73328 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 41070745-d4b6-3964-97a1-164a18a5836e | 1.67008 | -55.61346 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c15133ab-5dfc-33bb-8a6f-53c1eb5fbdd9 | -2.84928 | -59.11335 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e6fa28a-2e55-36aa-8a66-ed993b4a465d | -1.2176 | -55.65667 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 03e61aa2-b999-38fd-804e-90252961e761 | -2.50296 | -56.20342 | 2026-10-10 07:33:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2c5c0978-4866-3777-9879-f98dee4aee2b | -3.28926 | -53.86786 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 26ed5923-8096-3f73-91ae-29a4b6485d60 | -3.10583 | -53.78743 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b71e6943-4fa2-39bf-bb88-bff81d915ee4 | -3.03724 | -59.15361 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c753a890-4415-3b1b-b9bf-8b5bf8015fa4 | -3.57049 | -54.38359 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e8ef8697-d1ef-303c-8514-137c7f41c048 | -3.59869 | -54.60739 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 63358be5-2f3f-3f9b-bca6-79f809728fe7 | -3.57236 | -54.37102 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 31bc9e90-8750-38de-981d-c01546402d88 | -3.26667 | -54.06013 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9e84756d-9b14-3fb2-af17-70a256cd6216 | -3.24974 | -50.41676 | 2026-10-10 07:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| fadec0a3-8e7d-3f51-99f6-f61fc6eb97bf | -3.60047 | -54.59523 | 2026-10-10 07:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9e8340d5-7874-3f12-aad9-135d0864bb55 | -2.55989 | -57.4211 | 2026-10-10 07:33:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e07ef34-e66b-3939-aade-78c104e43c69 | -3.31867 | -54.00029 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6ff1f7d9-3c98-3a84-b771-d1ca4b29016f | -3.1655 | -58.62651 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| db477e62-7044-30be-b0a0-a64f0e8d3804 | -3.18306 | -58.6291 | 2026-10-10 07:33:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b5b57e45-5fa6-3825-8c9f-2d00e225bf3a | -3.03631 | -53.88759 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ad8e5b67-65d8-3ed7-af57-1dca5712339c | -4.40907 | -49.77975 | 2026-10-10 07:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 6dae5c9d-9687-3ea7-a6e6-6f80ef43e823 | -3.26059 | -54.17773 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 09566269-3b02-31e3-a55a-f3f967dec024 | -2.93627 | -54.09378 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f08b8399-3d23-32b7-a32f-c8fbaf26f092 | -3.11995 | -54.17173 | 2026-10-10 07:33:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c0088060-359f-3cd3-97a0-028b96fe5b09 | -3.30802 | -53.9988 | 2026-10-10 07:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 1e1b49d9-f38d-305f-ac6c-b12cd2d19586 | 1.73546 | -55.55936 | 2026-10-10 07:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b0215366-6bb0-3f37-aa13-360af0e81be8 | -2.83125 | -54.8075 | 2026-10-10 07:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 55365d46-70af-3881-bab1-9df28d1acde9 | -3.97832 | -59.36166 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f3d5a65a-f8bf-3ffe-a203-9394c56ced57 | -3.9797 | -59.35268 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f1ac6f7c-9ce9-399c-8398-02b543fcea9b | -6.32969 | -58.29892 | 2026-10-10 07:35:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fdf8b9ff-7757-39d3-9d68-c6b78cc08cb9 | -7.2196 | -55.06243 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5a39055e-8ece-3b52-b59b-5ea5878623c5 | -3.92193 | -59.66879 | 2026-10-10 07:35:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6428f7c9-8a89-3dd7-bc2a-aba3259b27b6 | -3.63645 | -60.62567 | 2026-10-10 07:35:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 245a7e59-7cae-3dd4-a85f-fc3b7bb62d71 | -5.19261 | -60.3092 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README150.md)
