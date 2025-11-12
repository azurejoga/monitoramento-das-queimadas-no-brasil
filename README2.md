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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b316dee-8745-3de5-bf76-2af3379f3fcf | -18.475401 | -53.386101 | 2025-11-12 00:34:00 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b3528c31-3aa9-3365-9a79-0aaa8e1d7e22 | -21.054199 | -47.238899 | 2025-11-12 00:34:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d59a7ea7-e70a-3eb6-9f3f-f3060f27c3ea | -23.5921 | -49.0042 | 2025-11-12 00:34:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| efdb438e-0190-3706-bbab-6a01a52850b4 | -19.777901 | -57.9534 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 029eb4fd-7261-3989-b876-43f1a96f5f6f | -2.3889 | -49.376499 | 2025-11-12 00:34:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5d85a2f-9611-355f-91cb-e6dff9430871 | -20.5065 | -47.2472 | 2025-11-12 00:34:00 | METOP-B | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 40b83cb9-9681-35f9-a028-f0e33e901646 | -19.719101 | -58.0191 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51ad2b10-9744-3288-b05f-db4910e84a29 | -4.1114 | -48.0131 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c87e2bf-2884-3c03-b968-a4a3766b9dca | -19.7533 | -57.985199 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7af4727-0dd1-3ca7-ad91-5a9f9a076451 | -3.898 | -52.107399 | 2025-11-12 00:34:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a36ad663-eeff-394d-9054-bd8522903232 | -3.0747 | -49.453602 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94316783-5f63-3650-b0b3-27a1b9a96444 | -20.887501 | -50.105 | 2025-11-12 00:34:00 | METOP-B | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 596a5919-03e0-3cb7-ae22-83249d01868d | -3.0735 | -49.492401 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18ac81d-a7fc-3e7e-b381-e2a2dd3c95ba | -3.4814 | -49.961102 | 2025-11-12 00:34:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569b5ccb-42d0-3449-9992-e0a502475a02 | -3.9507 | -43.756302 | 2025-11-12 00:34:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b9eac7d-859b-3b44-84e1-1501b58b9d12 | -3.7799 | -52.221001 | 2025-11-12 00:34:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecdc7415-84f3-395e-a99d-d97bf75c72f9 | -2.875 | -51.4701 | 2025-11-12 00:34:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7326be8b-71b5-3655-9c39-97f3f56cff6e | -4.0981 | -48.000702 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee723742-2b4d-3e98-a240-1bcff9fc24c2 | -1.1026 | -52.5826 | 2025-11-12 00:34:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a467f06d-e962-3812-807a-14a2ecabbe1c | -2.7987 | -52.972099 | 2025-11-12 00:34:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9400630-4657-3c3f-9042-d6fce0a32d11 | -21.42 | -48.6427 | 2025-11-12 00:34:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 078cba20-bb42-3af4-a670-ddd0212069cb | -2.9389 | -45.5504 | 2025-11-12 00:34:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 990cb4fe-2664-3d83-9c28-c92375223d60 | -4.0822 | -48.02 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09eacfc1-5794-31e6-926f-50d0b7591a43 | -16.8797 | -51.638901 | 2025-11-12 00:34:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63a398b7-80c3-310b-a4ed-33083343186d | -16.441 | -44.9935 | 2025-11-12 00:34:00 | METOP-B | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd7d470-ed47-3c8d-9f9b-30507b82eed6 | -3.2302 | -50.0308 | 2025-11-12 00:34:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb1dbab-3405-3798-92d3-88d8f58d4b93 | -20.8859 | -50.0975 | 2025-11-12 00:34:00 | METOP-B | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f150fa0-55e9-3146-9023-25adf124501c | -3.7059 | -45.808498 | 2025-11-12 00:34:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0e2af9-c825-3e1d-90fc-6309e730e41b | -17.8745 | -48.359699 | 2025-11-12 00:34:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64b480f4-b5aa-317e-bc25-62ea971c9cbf | -21.172501 | -48.691101 | 2025-11-12 00:34:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f0c5129-0c0d-3bf4-9098-09cecd03b88d | -15.5875 | -46.273602 | 2025-11-12 00:34:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23560203-650e-3d78-9138-e10e5de6b78d | -17.8766 | -48.368698 | 2025-11-12 00:34:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc52013d-c396-3e9a-8894-f311a7a14432 | -2.3919 | -49.389099 | 2025-11-12 00:34:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821eb596-6536-34a6-bd44-edb458721ea4 | -2.8632 | -51.4631 | 2025-11-12 00:34:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4081b86c-0a9c-3048-9ea5-bfbcec991096 | -21.056499 | -47.248299 | 2025-11-12 00:34:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 607c3337-429e-332d-b2d1-65b3042475b8 | -4.951 | -43.721699 | 2025-11-12 00:34:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20d40722-1fb9-30a9-b75c-00e04ba0947b | -2.8653 | -51.472301 | 2025-11-12 00:34:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9a7b1d7-31c1-3fb2-879f-a9259fb0ab78 | -2.6319 | -49.186001 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a610ba08-24e3-3ab3-a32b-2b89dee49ce1 | -2.5225 | -47.801102 | 2025-11-12 00:34:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 730b2b44-bf50-3f74-a17b-7e4657c9e1f3 | -20.895599 | -50.095001 | 2025-11-12 00:34:00 | METOP-B | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39743c54-1d71-3760-945e-a797f0f7050f | -21.4102 | -48.645302 | 2025-11-12 00:34:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 262bbb3c-c6b5-3bf8-8707-57de12f89236 | -4.0849 | -47.9883 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 050d68ed-ed98-3438-b660-09f85664f83b | -3.3231 | -44.0616 | 2025-11-12 00:34:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d0edf1-6c30-3a08-9e63-507e79e01899 | -2.4791 | -50.250099 | 2025-11-12 00:34:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a56dc88d-aa54-3cce-bd36-790f7fb00844 | -3.0776 | -49.465801 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236c14af-02c0-3786-ae1d-9f1d2871768b | -3.9579 | -43.7854 | 2025-11-12 00:34:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e48f229-c59b-3dac-87e4-a3899cdcfce8 | -20.2143 | -56.597698 | 2025-11-12 00:34:00 | METOP-B | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3feb9ec-7661-3f7c-ac33-5b662dd15be4 | -3.9693 | -47.288502 | 2025-11-12 00:34:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d24bbd0-8b1f-3d8f-b84a-50feae1ccdf5 | -19.8216 | -57.9715 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4cff12f3-d278-3e2c-99bf-a698b6b2ed68 | -21.810801 | -56.2854 | 2025-11-12 00:34:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 75cf80f7-8094-3344-9f75-163ddf5174d9 | -4.0919 | -48.0177 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd2a87c-faca-3411-9fc6-feeb1a8f8c69 | -2.6349 | -49.198898 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 132a4d13-fbe4-377c-9b81-d7ad81468542 | -16.8813 | -51.646 | 2025-11-12 00:34:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea3ffbc-5f48-394e-bad7-eb384126a6c0 | -3.6326 | -50.168201 | 2025-11-12 00:34:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6b0d5c-445f-3219-bb62-080938fb40df | -22.7852 | -51.6721 | 2025-11-12 00:34:00 | METOP-B | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d361d69-5a74-3122-8fdf-267841eef3bd | -19.799801 | -57.962502 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| df57ef05-2a28-3f68-9f1b-53db2e9f11ad | -19.846001 | -57.993698 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ff12282-ff62-38ba-9c3c-228779fd9b0f | -3.9458 | -50.318901 | 2025-11-12 00:34:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda5080a-c7cb-35fc-93a7-4d31d5d25aa2 | -4.1016 | -48.0154 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9800ed4b-2660-3eb6-9d4b-51c12b612bce | -19.811899 | -57.973499 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 834573ee-e3a0-347b-b4ee-318ad4794fef | -23.6017 | -51.305599 | 2025-11-12 00:34:00 | METOP-B | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c907377-fc9a-3761-a17e-b3877ab0d499 | -23.593901 | -49.012001 | 2025-11-12 00:34:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9ac4c14-956e-3ef0-a95c-9cc99a5b1e10 | -4.0946 | -47.986 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea8c591-8663-38d5-8076-74f198ab88dc | -19.750999 | -57.972198 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7795db46-0bcf-374e-baab-c99cf1d9e8c4 | -4.9414 | -43.724098 | 2025-11-12 00:34:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 048e87c5-fde8-3485-9270-9ee9d2107a72 | -3.8882 | -52.1096 | 2025-11-12 00:34:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362a6c5e-ec7c-35fc-b327-05bc8de61fbb | -4.0787 | -48.005299 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24128b0b-23ce-313c-9c8e-356e97d89f2d | -4.1078 | -47.998402 | 2025-11-12 00:34:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae972838-eb5c-361c-bfed-aecd9cb1d489 | -17.623301 | -46.701401 | 2025-11-12 00:34:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a275c5c-781d-3fa2-98ab-6c1016ebae20 | -19.7705 | -57.9683 | 2025-11-12 00:34:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4592496b-f533-372a-88f5-12b6f0816a80 | -3.0763 | -49.504501 | 2025-11-12 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c078114c-85b5-32e7-b185-bdb419f0e076 | -3.6962 | -45.810799 | 2025-11-12 00:34:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cee74f3c-62f1-3e49-8d5a-00c94c03f25f | -20.884199 | -50.089901 | 2025-11-12 00:34:00 | METOP-B | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8bc28da7-872b-356b-b66e-4cd3f54e0405 | -4.9643 | -43.7182 | 2025-11-12 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 555cc292-3faa-3e64-9fde-9feffb773041 | -4.1162 | -47.9919 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b38c0b5e-4fe2-33b3-b414-d2ccd8a91f2f | -4.1161 | -48.0136 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 318.1 |
| d46ac11b-89fb-3b1d-9fda-934c085245f9 | -4.7243 | -43.3157 | 2025-11-12 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 877aa6d1-79b8-3ddf-82fd-456a4a25aa03 | -2.8802 | -51.4835 | 2025-11-12 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7ce2da9a-dac2-3ec3-8971-f7b62ec90c77 | -4.0977 | -47.9927 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 728fbb0a-11d3-3e32-9c11-85448e8c04de | -4.9641 | -43.7413 | 2025-11-12 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d89fff5c-5c31-3771-8438-3776fbd74b02 | -4.0974 | -48.0361 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 641c3e74-dc34-3c84-a580-5659628092ac | -4.0976 | -48.0144 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 390.8 |
| be3737f5-a064-3380-828b-9df77ea376e5 | -20.8886 | -50.0937 | 2025-11-12 00:40:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 44ae6237-3681-3461-8635-acb2ab17f52f | -10.45 | -44.9746 | 2025-11-12 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 135da435-bf29-3609-9007-ca3bf9b6e95a | -4.116 | -48.0352 | 2025-11-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c78d10b5-c566-3aab-b688-36dbe32bcf2c | -4.9456 | -43.7194 | 2025-11-12 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 5bc22de5-6a2f-3ee9-8f9b-466c5ffdc471 | -6.5631 | -51.1126 | 2025-11-12 00:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| add9a1a6-3902-3e17-9a0e-799b83140f32 | -27.7127 | -50.06771 | 2025-11-12 00:47:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e2ef4f28-fedc-3b46-8cd9-9e9887a9f197 | -21.17856 | -48.69616 | 2025-11-12 00:49:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c8494480-8837-303d-9852-5a4e3eff56f0 | -21.06783 | -47.25356 | 2025-11-12 00:49:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4af2213a-e04e-3a01-a1a0-5d04d9258179 | -21.1668 | -48.68602 | 2025-11-12 00:49:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 23a50b38-6e5a-3a6f-9e30-e05fcd4438c8 | -20.8912 | -50.11238 | 2025-11-12 00:49:00 | TERRA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 79190ed9-ff18-3984-abca-e905b6f5391a | -21.81213 | -56.29507 | 2025-11-12 00:49:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 14159bac-01fa-32ff-86ef-dfffb5ef90b1 | -20.51516 | -47.26283 | 2025-11-12 00:49:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f5541e32-e951-36f8-aade-4cc141e1715a | -23.60722 | -51.31416 | 2025-11-12 00:49:00 | TERRA_M-M | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| cb29f6ac-9836-3500-a12b-3322b503a86a | -21.41717 | -48.6457 | 2025-11-12 00:49:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7fd53458-09c6-3633-a58d-099f758644da | -21.05703 | -47.25593 | 2025-11-12 00:49:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b4c77f41-bcfc-370d-b218-216dd146bde2 | -22.78267 | -51.6784 | 2025-11-12 00:49:00 | TERRA_M-M | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 114251fb-dffe-3f92-88f0-2a01c0b61ca8 | -23.59501 | -49.01567 | 2025-11-12 00:49:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 45db89ff-370e-3d10-8763-481b6303df73 | -20.89887 | -50.10046 | 2025-11-12 00:49:00 | TERRA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |


[Clique aqui para ver as próximas entradas](README3.md)
