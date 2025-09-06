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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbaf4682-7226-3f62-8fbb-edd304c1cd87 | -15.4431 | -47.134602 | 2025-09-06 01:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dabe5370-a11d-3bfb-996b-2dfe0855f89c | -13.0058 | -54.825199 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76c791ae-017b-3d71-970d-63f834d01cd9 | -11.6071 | -52.1828 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1fa929d-2996-367a-b91c-cc03853e7624 | -10.5906 | -44.313999 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c68f538-3456-3745-8809-9c8f040020bc | -6.0417 | -51.693901 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83777832-3e98-3622-8f8f-81947d6303c9 | -13.0009 | -54.849701 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc78bc12-8cc3-3a2b-ae00-7719bcbc6c9c | -11.5973 | -52.185101 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f42bc5ba-21c7-39ef-993c-70da8c43e635 | -12.484 | -53.862301 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3c725d-2cfd-3e70-96ad-c79106b33aa8 | -11.6137 | -52.211399 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2296e83b-6941-39fb-b684-675217ebb78e | -8.362 | -52.567402 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd51af77-2038-3b63-9fbe-8e24762ccda9 | -15.218 | -52.363201 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 433801c3-a44c-3d22-84d6-8cdccbad1d30 | -10.4386 | -53.611698 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d238419-3865-33c0-bfac-b40f4a528764 | -15.5414 | -49.831699 | 2025-09-06 01:05:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22e4040e-3810-342e-9b76-d32e99e1022b | -12.5134 | -53.855598 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90fba65a-ba44-3e30-8322-04737b8ce951 | -4.2709 | -48.1917 | 2025-09-06 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578bc1da-3940-3fdc-bfeb-9be0554d55ea | -13.7314 | -46.9202 | 2025-09-06 01:05:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae917bf1-5cdf-3739-94a0-e57a9802e286 | -5.0596 | -56.067001 | 2025-09-06 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58729a4d-5191-3ef5-8b84-6c8c66562da8 | -11.6393 | -54.552299 | 2025-09-06 01:05:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3b9373e-5493-3b74-924f-1e11e962fffe | -9.9668 | -51.656799 | 2025-09-06 01:05:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84d34556-6069-3cac-ae12-415c8fd624ff | -8.3551 | -48.292999 | 2025-09-06 01:05:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c302c8c-1e2b-3132-bec4-c40bef685622 | -6.8101 | -52.8181 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c070aa4f-f5ec-3e0b-a86b-65a73b10dda9 | -11.6005 | -52.154202 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3086438-4420-318c-91f5-db4d8ac9164a | -10.3121 | -51.455399 | 2025-09-06 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc375c19-d6d6-32a9-8bb4-99cfa0745bf7 | -14.5713 | -48.004101 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81ac5f23-5d85-3031-9f0e-8a28ff0cc625 | -15.8408 | -52.2906 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8a5656-a8da-3068-9001-ddfcdb74c8e7 | -6.8395 | -52.811401 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e56012-b3bc-3314-86ce-e9f4e120f17e | -17.7017 | -44.497501 | 2025-09-06 01:05:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d07d863c-87ad-3fe9-be52-65349e60d19a | -5.1969 | -60.027802 | 2025-09-06 01:05:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b097224a-587e-3f0a-96d2-cb1172b4888d | -7.7863 | -52.134602 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 011e6b4f-8315-3f9a-b0a7-57bcc8d71908 | -22.245399 | -48.773499 | 2025-09-06 01:05:00 | METOP-C | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d70657a7-34dc-3bc5-b294-4f5233fdcb8e | -6.274 | -53.444 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b35a385-6fd3-3ff2-ae7f-7ea985a4e9d0 | -14.7958 | -48.116402 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21222eb4-bb13-3ad8-9e3f-834dab1be228 | -8.3472 | -52.548 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff70abc9-6335-3e19-a984-f29fd844bbae | -12.4887 | -53.8834 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f90eb90-1325-3f21-9d15-52d20a2ddfce | -15.8554 | -52.309502 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb5f6c93-6c6f-304f-b1c1-e7f4a73d2f12 | -15.6971 | -53.5923 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb94422-171b-311d-9fb4-1646aa3f10fa | -9.7102 | -49.4911 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8afa7d6-1484-3eae-827b-1f17a723c6e8 | -12.4954 | -53.8671 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b623a9f3-f73d-3691-a861-7ff3c2479908 | -9.0532 | -50.456902 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dac012e-0766-3da4-9fdf-07e8f6605d4e | -5.9683 | -53.594799 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51742c0-11d1-32bb-a8a3-109a243b90ff | -15.5727 | -52.935299 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85c2c76b-79aa-3682-ba1e-c47115a6238d | -9.2457 | -57.076 | 2025-09-06 01:05:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eca2f28-30a7-3533-b8e7-057d0666466d | -6.7986 | -52.813099 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0044ea-87ef-3de1-99e2-768514d3e8a7 | -7.0542 | -50.866001 | 2025-09-06 01:05:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12bc03b9-4c4a-3e6e-8e9c-e5112f25db2c | -9.6757 | -51.121799 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa2326a-87df-3768-913f-5d03d1d509c0 | -9.9866 | -60.009701 | 2025-09-06 01:05:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f60fe4ed-f0b2-3c11-bd22-54283b3e59cf | -16.331699 | -52.968498 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a7e2e77-5194-3e5e-8e05-e0399151f854 | -15.0635 | -48.110199 | 2025-09-06 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db4f0b19-fd0d-32f9-ae2a-1a8ad95c5560 | -5.9415 | -53.791801 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde7bcdd-1309-303f-9a6b-2fe879ae9631 | -7.7224 | -50.333199 | 2025-09-06 01:05:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81f18b37-24ae-3ecf-84bd-bccb1c9481d0 | -15.5747 | -52.897499 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79cb1e2c-1102-3f0e-b7f6-de78ca72989e | -10.0816 | -48.089901 | 2025-09-06 01:05:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff77ac39-3111-3eb6-ba48-73058759ebc1 | -15.5731 | -52.8904 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 846c985b-4a6b-3889-91f5-d65120e810c8 | -3.3225 | -54.9175 | 2025-09-06 01:05:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc49c8b-bc84-3dde-8fa0-d1c323d24bc1 | -13.0026 | -54.810398 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46211a60-7130-3146-86d1-35589536a38d | -24.142799 | -49.523701 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| d30502c4-3c27-39b7-b200-8fe6b08b336a | -11.6021 | -52.161301 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de20f89b-a03c-3a56-8ad2-51a3c4e3c6f0 | -11.5342 | -47.319599 | 2025-09-06 01:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec4064aa-af85-36ad-9965-005f91fefd2d | -11.6038 | -52.168499 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab6d1aa-8ae9-3239-b90b-0247660c9af6 | -12.4711 | -53.850498 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f789810a-396f-3cce-94e1-8b11b4e25dcb | -6.7257 | -51.970001 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 148c6bc1-7bca-3f67-9d96-54f09be1d129 | -14.2504 | -52.1894 | 2025-09-06 01:05:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f9d75bc-0dde-3aee-85f6-057da17c0555 | -13.0091 | -54.840099 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b08ade5a-a1ba-3e62-8060-85da2f7e7626 | -9.6855 | -51.119499 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6457f939-6d4a-3e3c-b8e1-0dfd01527317 | -12.4856 | -53.869301 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1d6e09-4793-32e4-a6ec-2917509066c4 | -11.6054 | -52.175598 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06e16dc0-8d79-30d9-8d62-ca00493a496e | -8.3586 | -52.552898 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17225e0-3d18-31ad-8ff7-a4e9f144fe04 | -8.8539 | -52.020302 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5b6d937-79df-36a2-b4ca-3109ae7f6f9f | -7.7203 | -50.3241 | 2025-09-06 01:05:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed31717d-f94b-3844-975c-399c0f28d536 | -11.1997 | -55.028999 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c10600a3-3f69-3ae0-b861-bd4bddbbfa15 | -12.8957 | -48.896999 | 2025-09-06 01:05:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f66bdfe6-bf64-3d60-b05f-5786d9aaaacf | -8.0612 | -52.383801 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7cbefe6-f458-353a-ae65-803e73f73940 | -16.3172 | -52.949299 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d430e5b-20e2-3f39-bb33-0af76cdd0e68 | -5.8659 | -52.176701 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc226aec-d8d8-37c1-8866-912e03c0da35 | -10.6002 | -44.311501 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d3c8b0f-19ca-374e-9c8d-ecfe7391ce41 | -6.5663 | -51.116402 | 2025-09-06 01:05:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 761d9106-5f28-363a-a9a1-74165b217199 | -15.5825 | -52.932999 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f191cf7-ea72-381a-aea1-04722e4099d8 | -10.1284 | -55.162102 | 2025-09-06 01:05:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12ebaf0c-14c9-34fe-96a2-c6e5f5f54f8b | -20.524799 | -46.459599 | 2025-09-06 01:05:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efdfb9e1-d569-346d-8ece-d1ec6973cd45 | -12.5036 | -53.857899 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c27bea3-b0f1-3fde-ae94-e09e6f7758c5 | -12.4793 | -53.841202 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6427c342-cf23-335d-a06c-a18efb1074fd | -16.315599 | -52.942101 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20934fc9-d693-3439-a97c-c2e1fae81ea1 | -6.8003 | -52.8204 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ff82e5-a227-354d-b301-db1a566d3128 | -16.721201 | -49.397499 | 2025-09-06 01:05:00 | METOP-C | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7097cd-18fd-3491-a8e0-03418790b5e2 | -11.6121 | -52.2043 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12c8f04e-82cf-32eb-b487-98c73e26c743 | -10.1398 | -55.167099 | 2025-09-06 01:05:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e88da5ae-a9f3-32c3-aef6-ef1ec73ec0e6 | -9.0798 | -47.006401 | 2025-09-06 01:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff66c08a-86fa-3986-b91c-f84490aad296 | -16.290199 | -45.693699 | 2025-09-06 01:05:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 67784ae2-a897-3fe6-975b-f204d721405a | -15.7151 | -53.580601 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57c9cea8-0547-395d-b3cb-9d9de5780e8d | -16.305799 | -50.4884 | 2025-09-06 01:05:00 | METOP-C | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db3ceecd-d857-3c2b-978d-7f0a0bf26baf | -8.362 | -48.278801 | 2025-09-06 01:05:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3aabbe6c-1440-302b-b8dc-7a77b9030089 | -7.3208 | -48.4944 | 2025-09-06 01:05:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a865c85e-cbfc-30f8-8e68-ca5470ef3512 | -6.1792 | -53.257099 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bed88b66-ef7a-3dc9-bf4f-6363f561f5cf | -12.7792 | -48.1679 | 2025-09-06 01:05:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94b9c598-5b95-3a27-84d5-f9713c31b5d7 | -12.1822 | -53.894199 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfca69f7-a21f-386b-89f1-a035616a085b | -5.9529 | -53.796501 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fee04b9-c99f-3e91-a7dc-82d23a8f698d | -15.1656 | -52.405201 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 595b39e5-552e-3b48-b6ad-5c4efc411ac5 | -15.1804 | -52.379398 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b281f8b-c292-3e94-9c88-0758ba15354a | -5.4775 | -60.138401 | 2025-09-06 01:05:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c261e0c8-5e44-3368-843d-41075a9db713 | -22.253401 | -48.763 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README13.md)
