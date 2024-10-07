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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7199276e-af41-3d88-a9d8-ecd6f91ec96c | -21.63896 | -47.72511 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf09d6f9-9fb3-30bb-b99b-bc6b37771283 | -21.60507 | -47.71818 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77ad3691-11da-3c80-ae11-f9e77ab75bf5 | -21.60045 | -47.72202 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 450f7700-426b-3b41-888f-7be0b0d1b195 | -21.59864 | -47.73188 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a67978cd-ffe4-3500-8b58-0d472f88b1f3 | -21.59536 | -47.96477 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6760b326-b1a6-3a9a-976f-e63f1216e3ba | -21.59432 | -47.94881 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d62df7f7-d728-3ef4-9886-2f741a96dbd7 | -21.59397 | -47.73602 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2f82acb2-7054-315f-975c-05ffb7e5c513 | -21.59301 | -47.71997 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d30360b-b54b-3cca-ac48-f3faa2b28820 | -21.59114 | -47.73013 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 7e7a6e0b-0120-39fd-9652-3633ccb68226 | -21.59104 | -47.70946 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 490e6611-f74c-3498-9ed0-7da45fcaa3e2 | -21.59051 | -47.948 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f4b175b-550e-3db2-a3a1-b0687de1573e | -21.58959 | -47.95305 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efbf4682-57a3-325d-9a4d-dca383d4f4ea | -22.82873 | -48.42266 | 2024-10-07 04:04:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2e8e8e8-e7b3-3a42-91a0-9cd295974fbb | -22.80554 | -48.46172 | 2024-10-07 04:04:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f4d6bd9-7fb2-39c1-ada6-4984f01eaed2 | -23.44113 | -47.41031 | 2024-10-07 04:04:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9527d6ed-28a7-38f0-b0ea-b2aba47b67a0 | -23.44033 | -47.41482 | 2024-10-07 04:04:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b3d9eb09-0056-32a9-ae0a-48afad99c960 | -22.56515 | -47.49194 | 2024-10-07 04:04:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e2091d2b-e073-31f3-a038-7de917d20768 | -22.4831 | -48.36914 | 2024-10-07 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce7066a2-db1f-39cc-9614-58d85304f654 | -22.48211 | -48.37448 | 2024-10-07 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99807f0e-935c-394a-9832-9ee8bfef1d91 | -22.47929 | -48.36813 | 2024-10-07 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d12be3fb-c684-32fc-b73e-13a1e1f1d46c | -22.47828 | -48.37355 | 2024-10-07 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f7e4e3-f4ec-3b15-9a44-4834cc3bcbf5 | -22.38536 | -48.58865 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e6443bd6-0fd6-3120-85bd-ed23c1d03b04 | -22.38145 | -48.58787 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bba0939a-0c3b-3167-85ad-5a76b49d699a | -22.38115 | -48.59186 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| acaf284b-58ff-3464-a334-6a0839f79784 | -22.38043 | -48.59325 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 16feff73-cce8-30c7-827e-f5b5901ad4fb | -22.37724 | -48.59105 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d0ae4139-e4e8-3db8-8384-186714f9a936 | -22.37625 | -48.59642 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 956406c1-3d12-3fdd-b533-e585a215949e | -22.3755 | -48.59779 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e1260057-aa2c-3319-a0b0-a7ea93fc32e5 | -22.37527 | -48.60174 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7b6ef2d1-ed63-3854-b850-ae5640b6d429 | -22.37448 | -48.60309 | 2024-10-07 04:04:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a17dbfe0-869c-3cdc-bc91-2913001e75b9 | -23.85817 | -48.18688 | 2024-10-07 04:04:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08701a91-3f76-344e-9680-179437e73b86 | -25.19225 | -49.32723 | 2024-10-07 04:04:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cadf1fbd-dab7-3d10-8ec1-f912ccda598b | -20.6003 | -48.49358 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3adc8d98-b3c6-3b03-95aa-501f3dc8f547 | -20.5996 | -48.49731 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f87d87ef-9a48-35a6-8c7e-cad798a2fff8 | -20.5989 | -48.50103 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ffe6498-1a5d-3eaa-b514-f5bea67dc78d | -20.597 | -48.48902 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd24ade9-3e9a-3787-b963-e34b2aeac2e6 | -20.59629 | -48.49277 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed2ea18d-8dc7-3416-9d10-45a7c0c5f655 | -20.59559 | -48.49652 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f7ba340-3b45-36fa-bde4-31e8be62714d | -20.59489 | -48.50026 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b2e2e52f-104c-3087-827e-15d7f097cc76 | -20.59419 | -48.50399 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d8522be3-3a35-3e18-b29c-6f257853117d | -20.59349 | -48.50772 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 916ab2c1-82d8-3139-b164-8138a5e14bf4 | -20.593 | -48.4882 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05808223-8b2a-3db2-a54d-625fe3d98fd7 | -20.59229 | -48.49196 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb712446-7aff-374f-ac09-e53eb3f95614 | -20.59159 | -48.49573 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 83c04bd0-b93f-3441-97e0-d04f8b7e35c7 | -20.59088 | -48.49948 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f73790e2-af95-3d37-8c40-ad45d4447b9e | -20.59018 | -48.50322 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 225d176f-824b-33f1-a507-63fdbc7d9437 | -20.58948 | -48.50692 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 4362a1b6-9728-359a-aaa1-a6dfaf357a37 | -20.589 | -48.4874 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 888b666a-4159-3c69-9ac6-62b84877d809 | -20.58879 | -48.51059 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5e260c99-9100-3bc8-81c9-60af6ac047d7 | -20.58829 | -48.49116 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce14572d-6b2b-3b5b-96af-3798b7111d37 | -20.58758 | -48.49493 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6191bf6-58e6-35eb-a303-0d281fd74f34 | -20.58687 | -48.49868 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ae8b6354-469f-33f5-944e-f8166b05092c | -20.58617 | -48.50239 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5bfe5e53-5770-3065-91f8-4237def56841 | -20.58548 | -48.50607 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc488b09-68dd-30f4-9f0d-c1aa3eccf9c8 | -20.5848 | -48.5097 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85845c38-5be2-3c0a-8eff-a6ea5e008d19 | -20.58411 | -48.51337 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5485e137-4729-352b-a909-7ff1ddcb4d4c | -20.58341 | -48.51708 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e607e06-5867-36ff-bd23-f671fee0359d | -20.58288 | -48.49784 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9306b457-d9cd-3f50-a84e-248bce7ab382 | -20.5827 | -48.52082 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f52548a1-204c-3a19-8c24-f670ce43302c | -20.58219 | -48.5015 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 27201073-5e03-37ca-869c-99c221aa1a97 | -20.5815 | -48.50514 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2ecb0567-4223-38a5-a6e5-3e2ebda97c88 | -20.58081 | -48.50879 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f8a61b75-4b99-3d28-bfb5-b5798ef2eda1 | -20.58012 | -48.51246 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79006305-3813-3827-bdb2-51a6e5d55a2a | -20.57941 | -48.51621 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feb5fb60-f409-304f-b59f-73e3234e8d63 | -20.57869 | -48.52 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945e8d02-85ca-3e43-8fbc-4c1c73e95f44 | -20.57819 | -48.50066 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba85ad5f-8555-3273-83ee-c8d0f1eb0ed6 | -20.57798 | -48.52379 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9745b5a7-cd96-3d7f-b3c8-ce7ee2c69f1b | -20.5775 | -48.5043 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f7b77672-a137-35a2-85d4-c12339f71de7 | -20.57681 | -48.50797 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f1f1a35b-29c8-334f-9518-148e173d09cc | -20.5761 | -48.51168 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 73363d6e-620b-3576-ab15-ac88c860b644 | -20.57539 | -48.51544 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 543f1f3d-9e6e-302a-86d1-1c41fd61c7e3 | -20.57468 | -48.51923 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 947cf71a-9f6b-30e6-ac95-ce3f1c1b5d9e | -20.57397 | -48.52299 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69639f5d-e84f-3cec-9f8c-c4ecc0c3a296 | -20.57326 | -48.52672 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f75f5cc-ff20-32d4-bbbd-a9a571eee9fd | -20.57279 | -48.50722 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b36e4c1f-f497-37ac-b0ba-7ae5c9db9f8e | -20.57137 | -48.51468 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 41871b06-9a0c-30e6-bf75-ad5cf1aca7a8 | -20.57067 | -48.51843 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b0b30be-f401-3b24-939f-04949034a726 | -20.56996 | -48.52216 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb32b925-623a-3d4b-9242-51b2a756f038 | -20.56926 | -48.52585 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72f59632-98e3-321b-b627-374f431e009e | -20.75767 | -49.47841 | 2024-10-07 04:04:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2fbbca7c-f736-3c96-9170-ecbfcf716fe2 | -20.75686 | -49.48265 | 2024-10-07 04:04:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 048ebfe0-92f4-3f2d-b863-d58c86679525 | -20.75264 | -49.48169 | 2024-10-07 04:04:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4a92fcad-e274-3d35-b87a-b6349e71de6d | -20.74187 | -49.40084 | 2024-10-07 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d5688d-cefd-316b-97ca-45ce6dbc1989 | -20.7086 | -49.64062 | 2024-10-07 04:04:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e9c5c368-4ea3-3625-9fd4-09e27c6ada09 | -20.70775 | -49.64497 | 2024-10-07 04:04:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2428e4c0-26a7-390a-8dbd-9fad172b09e5 | -20.70432 | -49.63968 | 2024-10-07 04:04:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6dfcb2e-17f0-3495-a87a-6e1e56e7d2f9 | -20.70348 | -49.644 | 2024-10-07 04:04:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 485ce9f9-5566-3e8b-833a-98a7df1d5220 | -20.56991 | -49.36552 | 2024-10-07 04:04:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26f6259c-cf35-3d7e-9e75-e62d5481a3da | -20.4555 | -48.6382 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a1e7fd-57ab-332f-b769-8de00517267f | -20.45477 | -48.64208 | 2024-10-07 04:04:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7277ad0-452d-3a64-bc2f-fbbb2e6d303a | -20.19443 | -48.70768 | 2024-10-07 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c75f7cd5-c3dd-3dbf-b649-97e2a970bb00 | -20.18184 | -48.7291 | 2024-10-07 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40d0a3af-0c00-3d8c-bb43-54f9f5662c67 | -22.35697 | -49.03998 | 2024-10-07 04:04:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d25e235-fcbd-3ff3-8176-f42f13024d74 | -22.2846 | -50.00346 | 2024-10-07 04:04:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 744d6be8-8cd6-3360-bde8-10201d23798b | -22.2804 | -50.00228 | 2024-10-07 04:04:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6fd585a-d100-31d1-8689-9284f52cf189 | -21.99923 | -49.45295 | 2024-10-07 04:04:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4fa38048-2fea-3840-903c-2f2dc1881f50 | -21.61439 | -49.56357 | 2024-10-07 04:04:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f4cf565-c66a-3727-8a3f-5017bdea5554 | -21.29653 | -48.80817 | 2024-10-07 04:04:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 366fe315-ee43-3ea3-8917-2954bf6d9197 | -21.29581 | -48.81195 | 2024-10-07 04:04:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5249ca7c-6cfc-3507-ab71-a21cb384915e | -21.15223 | -48.9488 | 2024-10-07 04:04:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README71.md)
