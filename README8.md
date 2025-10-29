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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbcf1835-0b4d-3dd8-8875-c417ced3909e | -8.19653 | -44.44704 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77003142-9f35-3c34-a688-2fedf6679c63 | -6.1394 | -41.70879 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b4859e9-269f-3e44-9f47-0bbf8654a41f | -7.80393 | -46.44991 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| acf4e41c-d214-39df-92c6-513e2e7443fe | -5.96966 | -46.31992 | 2025-10-29 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1afe6894-9035-3fbe-afd2-efb0cc82895b | -7.79903 | -46.44922 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d92477c8-f818-3f45-81e1-fef63498c576 | -6.11649 | -42.4461 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| af2c3a26-a0d9-3f38-bd8c-1cab5e558fcf | -6.47994 | -42.24395 | 2025-10-29 03:53:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1c7e4c98-9764-3055-a3bf-0c5ea13a417a | -7.99079 | -45.54679 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfc07fe2-66c8-32c6-8452-9976e2a2f35a | -7.36618 | -41.59526 | 2025-10-29 03:53:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 55fe609a-4660-3fcf-a49b-abd1c20d6b0d | -6.13952 | -41.84878 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c19bdb92-bae2-3a5d-bcaa-4b38f105f71b | -7.43562 | -45.12134 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19167678-1a11-3a38-8c74-6ce8402df7a1 | -4.52868 | -46.03941 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62dbba44-25d8-3bd6-8762-5d493b3c023e | -6.80066 | -46.40652 | 2025-10-29 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c922f63-5f34-3e6b-9405-77314c41dfb0 | -6.12911 | -41.84265 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 928dfd21-ab49-314d-97b3-2ebc3a0dd06d | -7.85919 | -44.23375 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f67b69f-6cf4-3554-a358-71868ceee992 | -8.0294 | -47.39738 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbf83472-180c-34fc-b6fd-466a5a22ce1d | -5.47931 | -46.44047 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3801e2fb-01b3-3ca5-bbe6-b5dc3ee510f2 | -6.49654 | -42.237 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 386cba7b-bc5c-31aa-8b04-1c4ca6dc7f9d | -4.07777 | -42.92449 | 2025-10-29 03:53:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff04ca89-5c9f-3e8c-bb35-347e1afbb687 | -6.11671 | -41.70927 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 46977374-881d-31c5-976b-a573b8a5dbbf | -7.44098 | -46.60631 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd3a8f6e-9d36-36c8-8033-a6a9cf18734c | -6.90956 | -42.86656 | 2025-10-29 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a8ccdadc-1976-3396-a0a7-535ca35202b0 | -6.77284 | -46.38155 | 2025-10-29 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4076a44-1a03-3373-a2a3-977687e838ac | -3.71891 | -41.56705 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8aab59dc-9437-33db-9ae7-99c63d587dcd | -4.92165 | -44.01995 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee032fc7-75f5-3279-a04f-e23858a8d2e4 | -3.16188 | -49.25066 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d055c5-cf61-39e3-8325-6f107df8e325 | -6.42383 | -42.3253 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41e012ee-0b32-3a66-9122-9ad9c915c133 | -5.66338 | -41.104 | 2025-10-29 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45d16362-90dd-39ee-9719-46ae95277d63 | -2.77172 | -45.40037 | 2025-10-29 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b7dfb4c-40f5-3653-b276-10fc6c7a648e | -8.54874 | -45.70488 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e88e6c45-ae83-3fed-91e8-d8984698d752 | -8.54238 | -45.68557 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9e5afb5-4e15-3547-b248-dff6dfdbba23 | -6.64011 | -44.60854 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 676986e6-e03c-3fbe-b401-47940bf889c3 | -7.27712 | -46.88943 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36b29242-7cdc-3c13-b5ea-1f3e0931bf08 | -7.28085 | -44.1027 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 862078e8-f7a7-3bf6-afeb-77ae0473a1e0 | -5.39668 | -45.13236 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d896eaf2-f554-3b57-b288-0359f1d03014 | -4.99118 | -44.91285 | 2025-10-29 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c30342a-0d8d-3978-b677-aecf147bb51b | -6.29945 | -41.87677 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| de11dbdc-af43-3c3e-8b95-416c57b36ad7 | -3.15926 | -49.24768 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7cdd69e-0f38-377a-8154-4f516ee89575 | -3.38264 | -48.94768 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e91f1021-26c2-32b1-8ef4-6d4bbb83c47a | -6.1328 | -41.703 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4b974b01-35b6-3054-83ef-dcf33e15a027 | -7.40939 | -47.17146 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66d0afdc-5e2f-34e9-8f6b-dd37b098cf10 | -2.82913 | -49.4007 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaa78c48-fa74-3cd8-8f68-e91a7c332561 | -6.12767 | -41.85159 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e7c6ec33-8afc-33e9-a5b5-963a345e6fe6 | -6.14872 | -41.6745 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b965819-c2c8-3968-90d0-4acffc19e593 | -8.04072 | -42.51612 | 2025-10-29 03:53:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e117ba9a-b598-3dc7-91ba-e2c1953094b3 | -5.60001 | -44.96324 | 2025-10-29 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a921f9e2-f63d-3849-8769-2ea8a907bdb9 | -7.50409 | -46.74471 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35e81b66-bd4e-3c09-9218-69dd1537b372 | -6.96863 | -39.12147 | 2025-10-29 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a2bd091-fa40-327c-9b9e-93c757cc3aae | -7.81644 | -46.40739 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c566bc7d-1363-3303-abe9-1d182118d970 | -2.8308 | -49.40197 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62d33611-677c-32f0-95b1-3f8edf4cf0b7 | -6.30499 | -44.69334 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 69741d72-af00-38bf-b3ce-ff9b942e2e38 | -7.44617 | -39.26581 | 2025-10-29 03:53:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40c61494-a35a-3e5c-ae7a-6ff92cda9a0c | -4.6549 | -42.51829 | 2025-10-29 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 14d7c7fc-a79c-33ad-962a-cc9a647fe643 | -3.70883 | -45.38915 | 2025-10-29 03:53:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9ddb0c0a-eebc-3448-84a9-4be61bdad796 | -7.98997 | -45.55159 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c51d702-4a63-39f3-b71a-6836c6037e8b | -3.15559 | -49.24952 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65f11236-4a6e-327c-818d-df1c0b3ba1d2 | -5.18591 | -44.35581 | 2025-10-29 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32ef20d1-d97d-3452-910b-fe798991a45a | -8.14675 | -47.74344 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7bcfb9d-38ac-3d5b-936b-7ddb86120371 | -4.66228 | -46.40253 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1ac1e09-5c67-38c4-9e4f-05cc4db845f6 | -7.31937 | -47.19973 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3506adbd-f547-3dac-8221-6503ba29aebf | -3.71515 | -41.56644 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| af0c2091-877f-3d31-8a53-80d826734841 | -7.78534 | -46.46973 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ae1c170a-78d8-3440-bba1-6df9a383a930 | -3.5688 | -43.27787 | 2025-10-29 03:53:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86915a38-ce8d-306c-a237-c7bc3443cbd1 | -3.70784 | -45.38678 | 2025-10-29 03:53:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 399ae498-5dea-3bfe-8215-b695e79c7d07 | -6.03805 | -41.88738 | 2025-10-29 03:53:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 326fcfa6-4352-3bf5-ab5a-9267b951a74f | -8.54603 | -45.69168 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2636b385-d526-3f8e-8900-ed1b7fc9866d | -6.14718 | -41.56831 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 4495e781-151e-3e7e-8bff-c20efee3f6b6 | -8.04015 | -47.40529 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a50bfe6-9990-3cd3-b25e-f6563b3196d0 | -6.6415 | -43.57151 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd1e46f8-adc9-3ab9-83b5-0b141022f260 | -7.79804 | -46.4548 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9d75912-7ac4-3867-9edb-0f0dd8d97cf8 | -6.16127 | -41.82372 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 85b3e786-91d7-3555-af69-d0298e93c049 | -6.25188 | -41.80247 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5504600e-d823-3aae-aa82-e4577d6ab119 | -2.96353 | -48.59614 | 2025-10-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05d3508f-699f-3780-849a-a36d0e244e00 | -8.19231 | -44.44635 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b299bd-428e-3130-80e5-5c79206976ce | -4.21042 | -50.07958 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 58214fe9-c928-3a18-9154-97c09241f342 | -7.74304 | -44.72792 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dec40699-d1d3-3d29-88a6-e51ccdc0ea71 | -7.80773 | -46.42836 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08a8940e-7023-34fb-be60-2aaa7eb36a6b | -6.4638 | -43.55993 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 149f5739-4670-3854-83e0-df19c0c80d64 | -4.20286 | -50.08424 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 370016a6-0229-30b9-b949-701d2d5a6222 | -5.97515 | -46.3178 | 2025-10-29 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50527504-2218-3d19-b099-c918da929072 | -5.17843 | -44.92028 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54270219-88bf-3fc6-8f3d-a9b0cdf0555c | -7.07364 | -44.95787 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f7597a1c-311f-30c2-9e60-18f97cacb17d | -8.67016 | -43.92002 | 2025-10-29 03:53:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b823d7-6111-325a-8f56-96bb5e80ca4b | -6.49731 | -42.23228 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 035be20c-45e9-3a4c-b63f-e2bf1de1ec70 | -7.78338 | -46.45258 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 50a84159-4647-3d8d-8a2d-793b29c50a03 | -3.89095 | -40.80226 | 2025-10-29 03:53:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b65fda75-9d03-3c99-b43d-febdda96faaf | -5.52588 | -45.43503 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7c1bc38-2832-3d18-b7ec-1a04927011f9 | -8.0091 | -46.20906 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34b96000-d6fe-3f4d-9bbf-ad688eb05d1c | -5.33578 | -45.5428 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e67488a4-3d70-33a6-94a3-cff7325a2a8e | -6.11193 | -42.4259 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e73df8a8-dc70-335f-9e69-a267a39042ac | -3.89521 | -40.79867 | 2025-10-29 03:53:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cecd3064-c8c4-3522-a818-d0caf60d7bc7 | -5.19377 | -45.62658 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f05df86-77ad-351d-8628-004588f52cce | -6.70341 | -38.21029 | 2025-10-29 03:53:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fee1852b-5533-3e54-86f5-2961b9d40a87 | -7.27956 | -44.11046 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77c161fe-8d40-3c3c-b4fc-d60dadc1c896 | -6.59937 | -46.27787 | 2025-10-29 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c52e05c-3b5f-3c94-a638-45af96eb0ff8 | -6.29982 | -44.69703 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2616733a-6aae-3c67-b66b-60be6baef3b2 | -6.48447 | -42.23993 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 42246b77-58a8-30d8-98d7-1eaeea3d98d1 | -6.11017 | -41.7262 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6b7ca036-7b17-3233-bf11-9ecdbc69531f | -6.1494 | -41.57765 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 733d045a-abbe-301e-89ac-2698072d132e | -6.29503 | -41.88058 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README9.md)
