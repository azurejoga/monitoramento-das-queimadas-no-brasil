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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab9b9a5f-3094-3c21-b040-523d1d59950e | -17.95248 | -57.61637 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 030175ed-cb42-3654-b374-bbd14dfdbce4 | -17.95525 | -57.62056 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 04b203f2-d2b4-3fb4-aa71-ef1c92d8a483 | -17.89971 | -57.67103 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 934ef8ab-10cf-38f6-acef-49c82d7435e1 | -15.16521 | -56.83521 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dcc401c-c027-3739-a295-275de8b8dac6 | -15.26601 | -56.90697 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab031d15-7689-37ae-b524-9b9f58e42d31 | -19.03299 | -57.5377 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 11546b32-e8c4-316d-84f2-0ebc0ce036f3 | -19.02908 | -57.54084 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c6299d27-248c-3f2a-955d-00543c4519b0 | -19.02852 | -57.54455 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f3cd2a8e-97fe-39a5-9b39-eea3d51760a1 | -15.20118 | -56.86307 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7877cbf-cb6e-3548-bf78-7d83dc56dc77 | -15.20728 | -56.86777 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3eda788-ca57-3192-974e-3cd7e89805f3 | -15.15524 | -56.81142 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3e5252c0-3dbb-3a81-8081-774105863862 | -19.03576 | -57.54197 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f3491794-9434-3dd1-8d56-da738ee4a8bb | -15.19121 | -56.86138 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e8c3a3-5702-381b-8e1e-e54ee4cb8474 | -17.8925 | -57.67355 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 08217745-95a1-3f3d-9576-63290bca076a | -17.8465 | -57.66615 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e5a19cd6-848a-3c10-a5a9-ef8fed45075e | -15.87859 | -56.76026 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25321af7-ed05-374a-b8b9-d30e325fb546 | -19.0224 | -57.53972 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3a3e516a-b2e9-320f-a569-8b3cb1116838 | -15.75867 | -48.98104 | 2025-10-12 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cf02f07-902c-3804-a2f4-8a0a95479dd8 | -15.28552 | -57.08683 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 334fa39d-8ac7-3c4e-857b-cab7f249915c | -19.03242 | -57.5414 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 34606407-58a1-3b0e-9a8e-6ad4c15d82e9 | -17.81834 | -57.62781 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 133f98e1-657d-34d6-b057-d88628c37690 | -15.19786 | -56.8625 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a235fc89-831b-38ba-abfe-9c949451827f | -17.81615 | -57.61994 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bf355cfa-8a79-3443-83e3-6889b1c9bbb8 | -15.86187 | -56.75759 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dded3213-190d-359d-8fd3-52d4323f01a2 | -19.04579 | -57.54366 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| f53cdd7d-3523-3fde-819f-6ddc231fe9fb | -17.83709 | -57.66087 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a505534d-1a4e-3d1d-b4bc-c97b9d29f7aa | -19.03967 | -57.53883 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a7446fa0-4001-3b2a-8142-9cab31c57226 | -17.81879 | -57.669 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bc328a45-b65b-3940-8ace-4e45514636b1 | -17.89639 | -57.67048 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 417990be-4200-3748-bb67-42270b473bc7 | -18.55016 | -46.94728 | 2025-10-12 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a6f25e6-ac33-3f48-ab2b-d93aab2b7dc6 | -17.83044 | -57.65979 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77c85da9-7948-3f00-9444-ff7a64c40d65 | -17.82211 | -57.66955 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5ab4ee36-6a30-3c12-ac3f-d7682bfafa63 | -18.39883 | -46.39337 | 2025-10-12 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7918e6fa-3eca-37f9-8452-2a1ef144adfe | -17.83265 | -57.66757 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6f9e7e93-16f4-3002-a5d7-a6b83efd2db3 | -20.56517 | -54.63143 | 2025-10-12 05:06:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 925741cf-faf1-3377-b8d8-7cdf89e4af3b | -15.23331 | -56.87588 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e77d8573-a90f-3e95-9387-915b0b02cc42 | -15.20063 | -56.86664 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cad0cef-2424-31c4-aa48-4049a438898d | -15.85574 | -56.75286 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a70d4c-8645-339c-b9ff-f7dca55cc1cd | -15.23054 | -56.87174 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 872892d8-fc44-3dc7-acb4-48d0eab047c4 | -17.89526 | -57.67775 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 801ead5f-7445-3377-9fb4-9e130b67d807 | -17.89915 | -57.67466 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2444ce40-224a-3578-88fa-cc3662ec1a0d | -15.28828 | -57.09096 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13f21172-0cd4-3366-a4b1-396e2f2ea9c5 | -15.2894 | -57.08379 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbabea41-a2dd-306c-961b-06899565215e | -17.81214 | -57.66792 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6d161575-8357-3a05-a010-e01777ec181b | -19.0263 | -57.53657 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 52379001-6065-3179-8e8b-609c45422a2a | -15.1973 | -56.86607 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64556850-9eed-32d8-8f71-77307aba9a0a | -17.81607 | -57.64251 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6a73b5e4-467b-3121-9b50-835812dbf142 | -15.2178 | -56.86589 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 524570a5-e06a-3c8b-9ed6-dc2337911760 | -15.16742 | -56.84295 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c07667a-e84a-3687-8558-91a2a1ea91a5 | -19.02518 | -57.54399 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 47ef2ff2-252f-3947-acb5-ba53c4325ec4 | -19.04245 | -57.54309 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| f1bbb78c-21a2-3f50-b6b3-dfe8264b66ab | -17.86448 | -57.57205 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 24863afa-b8fe-3538-a8a3-d3daa6bcf5b0 | -15.75834 | -48.9839 | 2025-10-12 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6cc788a-06c9-3143-a322-f4ccc89e5722 | -17.81891 | -57.62415 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8509d401-c690-3687-bba5-93bad2d8661c | -15.29216 | -57.08792 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d382e1fa-f550-3a2c-8451-1470887bb5f4 | -15.87191 | -56.75919 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f06300b-b26b-375b-a431-112475579787 | -17.81778 | -57.63148 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6dfba3b1-5e4e-30b8-969a-447326f2841f | -15.18788 | -56.86082 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbd9818e-440e-30dc-83b8-6c8a89cc4a4c | -17.40727 | -46.87069 | 2025-10-12 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d4da390-726a-370f-a263-01c56080ded7 | -17.90027 | -57.66739 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e3c63122-bcb6-3c22-9081-17d7ec7d8778 | -17.83653 | -57.66449 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 289a319e-bcb2-3f5b-bd73-49f16c7d2ca9 | -17.82988 | -57.66341 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 809c6615-9c1d-3b49-93d9-c3a10248951a | -19.10204 | -46.41047 | 2025-10-12 05:06:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06de4ab7-9c7d-3b9e-8f2d-00ccd75edc2a | -17.94415 | -57.62617 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4399344e-001a-3adc-a949-d36373cd1c64 | -17.95079 | -57.62729 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4417f253-ba08-301f-b960-66ce7ac73591 | -17.25251 | -52.26646 | 2025-10-12 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1393c95-cc9d-3fa8-a7a4-80890b5b8bb8 | -15.15136 | -56.81445 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74195191-5df6-3df0-a7e9-616219f50c02 | -15.33958 | -59.18595 | 2025-10-12 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f172a4-a8c6-3b16-8a13-83f355866d80 | -15.86856 | -56.75865 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fffc733-999d-3bb0-b016-46a5dd993a38 | -18.55621 | -46.94797 | 2025-10-12 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dba99c9-b444-3b9a-946f-1908ec61ad72 | -15.22833 | -56.86393 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0118592-4a93-3a38-8a39-07049a9ac099 | -15.00377 | -53.88594 | 2025-10-12 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ecc4d97-9500-3a86-9abb-2672233fed9c | -17.81269 | -57.66436 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c127bf29-b6b3-3b9c-b754-c235e9f78954 | -22.03813 | -55.16784 | 2025-10-12 05:08:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c54c50f-2d1f-3ba9-b507-a95252a32098 | -23.59125 | -54.74221 | 2025-10-12 05:08:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 37e83c9d-a400-379e-a046-8a191f663b31 | -22.06015 | -55.9783 | 2025-10-12 05:08:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a832271-32ae-3325-9830-b3363e8c70f1 | -7.54442 | -43.83394 | 2025-10-12 05:46:00 | AQUA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e93caa7-9085-382c-ba00-2206ae158cbe | -3.51449 | -45.8386 | 2025-10-12 05:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d8bd0910-ae84-3bc4-ac0a-7a14b8488443 | -6.75377 | -44.65049 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 570d1b3a-e583-3c0b-8901-2a827fb6f3a8 | -5.91308 | -45.43053 | 2025-10-12 05:46:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9446c0dc-98c5-3221-a9bb-3bddebc6df5b | -6.24787 | -42.91907 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6709b7a2-8a48-3f61-828c-43aff518017f | -7.5057 | -44.63739 | 2025-10-12 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e0daba3-5613-3f04-b063-7dc32d81c96a | -7.19848 | -45.49029 | 2025-10-12 05:46:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| afb23089-d1c5-33e0-be81-1e9506a21e7f | -6.22077 | -42.66081 | 2025-10-12 05:46:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6ae05b6d-62c2-30ca-905e-499ab04d60b4 | -2.42816 | -49.3682 | 2025-10-12 05:46:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5bebb8b2-774a-3087-96f7-e0345e7cfdc5 | -3.3401 | -42.15361 | 2025-10-12 05:46:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 11.9 |
| cc7bf483-4752-3a5d-8314-85dffaa240c7 | -7.85455 | -44.5266 | 2025-10-12 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb51f5a6-c758-3a28-b4a3-a83cd2b3c7bf | -2.44063 | -49.36505 | 2025-10-12 05:46:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3e4b54b7-fa8d-3939-92f9-0756fcbca4de | -3.87054 | -42.5109 | 2025-10-12 05:46:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 41a8653b-3527-368c-a2d0-54df5067ab8d | -7.64723 | -42.57201 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f4420833-684b-3fd3-91c0-d2866de6b18e | -6.58535 | -44.61021 | 2025-10-12 05:46:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 941606f5-bc87-3287-8375-db1f541380ad | -4.67394 | -43.25681 | 2025-10-12 05:46:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b1d9497-dfa1-3d4d-ae9d-e76715278d46 | -7.74463 | -44.20897 | 2025-10-12 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7867f08a-74c0-31c1-8850-1d675b7d0c0f | -6.76096 | -42.82877 | 2025-10-12 05:46:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1178e67f-61ab-3a78-a673-59cdeee4917e | -7.05706 | -45.20949 | 2025-10-12 05:46:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 65a48dd1-88af-3669-9e4c-b566ee136049 | -6.76228 | -42.81981 | 2025-10-12 05:46:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ee9a2d67-c8be-3765-b508-6ce50d3a477c | -6.75512 | -44.64161 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3aa8a49-51a9-3ac1-86cd-0b5130de80f7 | -7.51112 | -44.60189 | 2025-10-12 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 94fc94bc-168a-30ef-b546-70232c8c9027 | -3.51289 | -45.8492 | 2025-10-12 05:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 04a40229-864e-38aa-9d8b-b9f0b1a8779d | -6.58399 | -44.61913 | 2025-10-12 05:46:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |


[Clique aqui para ver as próximas entradas](README43.md)
