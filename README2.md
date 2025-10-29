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
| 63fb6aa9-0017-3cf7-b964-b8e9038645db | -4.2157 | -50.0812 | 2025-10-29 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 764b70d7-8bc1-3f7c-8235-4022d9bce255 | -13.2266 | -47.0614 | 2025-10-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c1771a17-2331-37c9-9b92-daffede44a99 | -12.0032 | -46.7892 | 2025-10-29 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| df80faf5-e64c-345b-9d00-ec33063a34d7 | -10.6506 | -48.009 | 2025-10-29 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 72d1ea7d-7a20-33ea-8eca-cf0dc5adf8cb | -10.6509 | -47.9869 | 2025-10-29 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e41d2772-cc08-3953-93b5-516e5207b4f6 | -13.6426 | -46.4976 | 2025-10-29 00:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a06ac255-07b7-36c2-ad68-2a95fa8634bd | -4.0852 | -46.9458 | 2025-10-29 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b98f5fe5-fbe9-3b02-ac0d-eae9ae07b631 | -4.2157 | -50.0812 | 2025-10-29 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5857c4bc-3a97-3004-9063-049d82daba23 | -7.7849 | -46.4475 | 2025-10-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8ee3a87e-0d4c-3a02-9e00-ec34f4a0503d | -9.9358 | -47.6716 | 2025-10-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 25a302f8-5be9-3b79-a4ab-61177b2b6c58 | -13.2073 | -47.0643 | 2025-10-29 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 9884c93f-e955-3e41-9ed4-f64342edacc3 | -7.7847 | -46.4698 | 2025-10-29 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 791a03df-5a23-3840-9107-574acd5c27f6 | -7.8037 | -46.4458 | 2025-10-29 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d53be36f-bcf8-317e-a7f6-c6d63c909634 | -6.2936 | -41.8984 | 2025-10-29 00:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 6b0bb13f-f20e-3937-8f2c-46135be65dfc | -2.4263 | -49.3161 | 2025-10-29 00:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e7603817-646f-314d-9bee-cfea090a07a5 | -20.4767 | -42.0157 | 2025-10-29 00:50:00 | GOES-19 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 28417e72-bb84-3890-a8c9-b163b7a7321f | -9.9169 | -47.6737 | 2025-10-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c851c203-cd75-3306-ac0d-c2f692d7497e | -12.0036 | -46.7667 | 2025-10-29 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| b24856f3-44fd-3ac8-a832-0d37b354568b | -2.4264 | -49.2948 | 2025-10-29 00:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ac0d0c1e-6cc0-3852-baff-97f89232d52f | -13.6431 | -46.4748 | 2025-10-29 00:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a99de9ac-1144-351a-bf0e-931be460dfac | -6.3127 | -41.8727 | 2025-10-29 00:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| d25ceebb-0c64-389f-8408-b4698ff1c875 | -12.0032 | -46.7892 | 2025-10-29 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d1c10abc-1d56-3421-ad8d-1bc8aeed4076 | -3.2762 | -45.3353 | 2025-10-29 00:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 924a0edc-e1aa-3fe9-9ec7-f577b0b96dbc | -10.5467 | -49.9973 | 2025-10-29 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d588fd57-0449-3ea6-b7e3-7ba9aabe4055 | -3.0507 | -50.2702 | 2025-10-29 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| de501cbe-4eda-3f11-b75e-6825fb625808 | -10.6506 | -48.009 | 2025-10-29 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| eb7ebdee-6911-3c97-8df3-dd7424e533bb | -6.3125 | -41.8967 | 2025-10-29 00:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| fc48775b-191e-3d1b-bb1c-37b243efd619 | -13.6426 | -46.4976 | 2025-10-29 00:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 9dc4c4c3-ef75-3ad1-a6a3-30216ece37ec | -6.2939 | -41.8744 | 2025-10-29 00:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 181.9 |
| fcb07b26-99ad-3007-aa60-5f2a1f428e75 | -10.6509 | -47.9869 | 2025-10-29 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e198a604-85fb-349a-acf6-4e508e6e3ecc | -6.3125 | -41.8967 | 2025-10-29 01:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| f1dbf7ae-5de9-357b-ba20-cf005b7fe5fc | -2.4263 | -49.3161 | 2025-10-29 01:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 18dc3bf1-a2cb-3f1e-be14-2acd73f40d60 | -10.1923 | -36.6968 | 2025-10-29 01:00:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 71.4 |
| b45d72cc-9293-3b96-a07c-756da2cc9467 | -6.2939 | -41.8744 | 2025-10-29 01:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| c2ed2649-cd9f-30b2-b8de-b927a761072c | -12.0036 | -46.7667 | 2025-10-29 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5489498f-d403-3d06-8cef-efe7bddf5929 | -13.6431 | -46.4748 | 2025-10-29 01:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ae548f2a-39e8-3c5d-87b8-ea403b51cc9c | -12.0032 | -46.7892 | 2025-10-29 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5a15b8a7-fd0a-326f-b13e-1d111914a428 | -6.0739 | -47.2922 | 2025-10-29 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 170d98e1-ea0e-391d-8397-1b05ff69facb | -13.2073 | -47.0643 | 2025-10-29 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e61e6422-3546-399e-9e61-e94524d54d3e | -2.4264 | -49.2948 | 2025-10-29 01:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0391bfa1-9332-3cf9-bfba-2b0d8a81a54a | -4.4804 | -43.447 | 2025-10-29 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5d30fe66-d4ef-37f3-9a36-64197b32de82 | -12.1958 | -46.717 | 2025-10-29 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 728b8d23-81a0-3333-a65f-e31e8e2fd224 | -6.2936 | -41.8984 | 2025-10-29 01:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| f313d46f-05ff-358a-ba01-14182956a0d2 | -4.1972 | -50.0819 | 2025-10-29 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8d732f76-708f-3474-aeb5-56f197324c45 | -6.3127 | -41.8727 | 2025-10-29 01:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| 19378520-f062-39a6-b172-78d14823f3d0 | -18.0739 | -42.9959 | 2025-10-29 01:00:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| c913a96c-cf64-38c9-968d-a2b585c31d98 | -10.6506 | -48.009 | 2025-10-29 01:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 55da4355-18a8-32bc-b630-d1282e88995a | -7.8037 | -46.4458 | 2025-10-29 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e3e8b602-eaa7-366d-bc2d-f26275a102e5 | -10.6509 | -47.9869 | 2025-10-29 01:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 7d31ace1-f051-3a6d-8348-706e3f09f35c | -13.6426 | -46.4976 | 2025-10-29 01:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| d22bfe2a-249e-3a74-b980-8d5951ce6886 | -4.2157 | -50.0812 | 2025-10-29 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6bad69b7-d75c-3d18-b496-08b86d79877e | -16.3365 | -49.8846 | 2025-10-29 01:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 629c905e-ee93-3fd5-88a8-c2a6078d926d | -6.2936 | -41.8984 | 2025-10-29 01:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 8b26a984-53d3-3fe2-9845-0efc8ff4af12 | -2.4264 | -49.2948 | 2025-10-29 01:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1b76a9b8-c053-3fa6-81db-18e79ad1a185 | -15.1006 | -43.8333 | 2025-10-29 01:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| fcbdb4e0-5ede-37c3-849d-cad20cc4a4fe | -10.6509 | -47.9869 | 2025-10-29 01:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d6d9f426-ca2d-3af5-936e-f7abf8eb6486 | -13.2073 | -47.0643 | 2025-10-29 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 679e89ca-6b74-3aff-962a-57c314f57ef8 | -6.3125 | -41.8967 | 2025-10-29 01:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 757750e8-db16-3ce6-998a-c5509bf97226 | -10.6506 | -48.009 | 2025-10-29 01:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d9407635-ee10-3e9a-b880-39b28afe6dc3 | -12.0036 | -46.7667 | 2025-10-29 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 32db78c1-3e95-35f8-917c-dcec202d9b69 | -6.2939 | -41.8744 | 2025-10-29 01:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 188.2 |
| 74829fd9-6ff5-3142-ba3d-5bc2939a8076 | -6.3127 | -41.8727 | 2025-10-29 01:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 6bb7f1f2-83e6-3a3d-9962-f017a81b72e8 | -13.6426 | -46.4976 | 2025-10-29 01:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| b3627561-4a36-3fd0-b36f-eadee801fd16 | -2.4263 | -49.3161 | 2025-10-29 01:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3c32814c-e97c-3a78-957b-b3769a16a611 | -4.2157 | -50.0812 | 2025-10-29 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 134ea817-a5cf-3593-959e-c90c27e2604b | -4.5188 | -45.9937 | 2025-10-29 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a45d13f1-8fa9-3f9d-87af-e0fa0e61b9b2 | -7.8037 | -46.4458 | 2025-10-29 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b87fbc4b-5c23-3c55-aa23-1e0414e7da4b | -18.0739 | -42.9959 | 2025-10-29 01:10:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| bad77ac2-b0e8-3be1-8831-fb36e54adabc | -12.0032 | -46.7892 | 2025-10-29 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d9dd0379-bded-395e-92de-5e6a21b11eca | -7.8037 | -46.4458 | 2025-10-29 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4e9dd0b4-f1cb-3630-8f45-779a809232c8 | -12.0036 | -46.7667 | 2025-10-29 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 804b0607-efde-35c8-ab13-71b6710136f9 | -15.1006 | -43.8333 | 2025-10-29 01:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 82250734-af44-3e12-8071-c1772de2f23d | -6.3127 | -41.8727 | 2025-10-29 01:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 441bcc64-ecab-3f0b-b49a-461825993283 | -2.4263 | -49.3161 | 2025-10-29 01:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f623c25c-5d66-3603-9fd1-32d3a7a2d0fa | -10.6509 | -47.9869 | 2025-10-29 01:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 497b053a-4f8e-3786-b14b-411a621a35c8 | -4.2157 | -50.0812 | 2025-10-29 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f6d761b8-8414-3747-afa2-240521109bdb | -6.3125 | -41.8967 | 2025-10-29 01:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 4232b0c1-97a5-37bc-9639-70af8f4f0b28 | -4.4804 | -43.447 | 2025-10-29 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 4d5c2a59-2e69-381d-a2ce-658369ca4612 | -4.5188 | -45.9937 | 2025-10-29 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 37c27ed2-3b45-3e5e-b190-80afc68027ab | -10.6506 | -48.009 | 2025-10-29 01:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 4ce0405b-5dae-3a3d-b4f4-2abe9b952743 | -10.2071 | -45.9412 | 2025-10-29 01:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 6c9df4ce-1a47-343b-9bbe-746577e6065f | -12.0032 | -46.7892 | 2025-10-29 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1d50bc6b-2d3f-33a2-b36f-fbb825427457 | -13.6426 | -46.4976 | 2025-10-29 01:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 39e6f9bf-4202-34b0-8cff-63af04bc94fe | -6.2939 | -41.8744 | 2025-10-29 01:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 61db0f72-433c-3c9e-b72a-44f680e1572e | -6.2936 | -41.8984 | 2025-10-29 01:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 061128ae-1083-314d-a0c0-c2e5ab2abad0 | -2.4264 | -49.2948 | 2025-10-29 01:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5f928b0f-19b0-326e-b545-fd2986741a5b | -6.5631 | -51.1126 | 2025-10-29 01:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2c1bd3ec-b70e-3592-9078-b6b0f0240fc6 | -12.1958 | -46.717 | 2025-10-29 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| addf2ad6-4b66-3594-8ebf-24c2bf049280 | -13.6426 | -46.4976 | 2025-10-29 01:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b3f35700-b9c2-33ad-90bd-60587367bf13 | -10.6699 | -47.9847 | 2025-10-29 01:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 04622cb3-94c9-334e-9ed3-947f3d3728c0 | -4.1972 | -50.0819 | 2025-10-29 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7c905c89-7f00-3ca1-a26c-d42db9926b23 | -4.2157 | -50.0812 | 2025-10-29 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 807d9276-8e24-3292-9512-ee77b011d972 | -12.0032 | -46.7892 | 2025-10-29 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b6b4e021-9774-39ca-97b3-a41fb89aae73 | -10.6509 | -47.9869 | 2025-10-29 01:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 444c5ebc-f529-3cf4-9f24-9b04a3d54309 | -10.6506 | -48.009 | 2025-10-29 01:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9a5985bb-0c16-3a53-97bb-9617578edb3c | -4.5188 | -45.9937 | 2025-10-29 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8ba94c6d-42c8-3285-b205-6d10aa26db79 | -6.3127 | -41.8727 | 2025-10-29 01:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| c04b6e41-9006-3dcf-936c-fc4bec6545db | -12.0036 | -46.7667 | 2025-10-29 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3afc4074-6e37-3049-b436-44b8dd732d16 | -4.4804 | -43.447 | 2025-10-29 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| bd0a0694-247c-36cc-8634-2d87b191410e | -15.1006 | -43.8333 | 2025-10-29 01:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README3.md)
