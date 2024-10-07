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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6ce9e3d-8fbf-3815-ace8-bf9a274f5ccc | -20.4661 | -47.6592 | 2024-10-07 00:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fdbefb00-b6a9-3cfb-a85d-0980bf8b88ce | -20.4866 | -47.6544 | 2024-10-07 00:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 23dbed9b-4936-39d3-9afb-d4ee0967ce6b | -21.0712 | -47.2331 | 2024-10-07 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 93b620c1-07f0-3759-be37-8abd592d5290 | -21.0719 | -47.2094 | 2024-10-07 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2b8508a9-f1e5-34af-a4b8-549ab03b1779 | -21.0919 | -47.228 | 2024-10-07 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 6992e594-cc98-3783-8e2d-031f55fac0b7 | -21.0926 | -47.2043 | 2024-10-07 00:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a7aa00f0-2c4a-389b-9936-c8f9f554db9f | -21.2924 | -47.3908 | 2024-10-07 00:17:03 | GOES-16 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| e4dac312-2425-3a61-83c6-6e0abfa3bf42 | -21.5843 | -47.9536 | 2024-10-07 00:17:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 4a88abaf-7fd5-3b78-a5a2-2b20c334e1ba | -21.585 | -47.93 | 2024-10-07 00:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3503b092-a9b3-3318-b684-e8a4bcac06f5 | -21.605 | -47.9485 | 2024-10-07 00:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 384c5cce-8580-356e-9bad-93cf2f0f31c8 | -22.1974 | -48.1778 | 2024-10-07 00:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 191.0 |
| dc208f67-c276-3b5b-910f-e67890533592 | -22.1981 | -48.1541 | 2024-10-07 00:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 111.6 |
| f9d8a666-0b78-3cd5-9a29-18f2166fc8de | -22.2183 | -48.1726 | 2024-10-07 00:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 9bb5c933-6cc2-3aa0-90f0-7ffa89d7752c | -22.219 | -48.1489 | 2024-10-07 00:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 50df116b-3c36-342b-af87-1e956a374cc5 | -23.442301 | -47.036701 | 2024-10-07 00:24:20 | METOP-B | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e38c3184-8772-32b2-9003-fd998f47aec0 | -23.163799 | -45.534401 | 2024-10-07 00:24:20 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f11039f-d881-3765-8ab6-53050ffa6535 | -23.1654 | -45.542801 | 2024-10-07 00:24:20 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71baf0db-c97b-3ade-bf0d-89537d444f17 | -22.6262 | -44.144798 | 2024-10-07 00:24:24 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 341968d8-6f0a-3cfa-a798-a61143f86e3c | -22.52 | -44.225899 | 2024-10-07 00:24:26 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f425388-3205-391a-b151-b4745bd5f74b | -22.521601 | -44.233501 | 2024-10-07 00:24:26 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81973d56-bb42-3e31-83f5-7c9dd1db83ab | -22.0287 | -42.880901 | 2024-10-07 00:24:30 | METOP-B | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b275d5c3-a4a3-34c8-aa73-027ab6695e82 | -21.801399 | -42.501099 | 2024-10-07 00:24:32 | METOP-B | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c00b451d-39fb-3b41-8379-216375aefa2c | -21.7868 | -42.4813 | 2024-10-07 00:24:32 | METOP-B | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a24f572-a869-31af-a7e3-c7cdfb89dcca | -21.7017 | -42.282902 | 2024-10-07 00:24:33 | METOP-B | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 554b78f1-6983-3375-ba63-0c002e4d6c4d | -21.7033 | -42.290401 | 2024-10-07 00:24:33 | METOP-B | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a04084df-fad5-3225-87ba-20ec757b7459 | -21.5368 | -42.190498 | 2024-10-07 00:24:35 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f839232e-0a45-3445-a97a-2843b6e5bbbc | -23.0403 | -49.823898 | 2024-10-07 00:24:35 | METOP-B | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfbefe4a-69b3-34b6-a3bf-ae3f98c378d5 | -21.669201 | -43.987301 | 2024-10-07 00:24:39 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b22fdc6-f696-39cf-acae-ca408fa9ad54 | -21.9506 | -45.348301 | 2024-10-07 00:24:39 | METOP-B | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e6a3b50-8e38-3d32-b5f5-d2f02c002c22 | -21.952299 | -45.3564 | 2024-10-07 00:24:39 | METOP-B | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfad4637-ba6f-3aeb-a0df-2a2ef42d36ce | -21.953899 | -45.364399 | 2024-10-07 00:24:39 | METOP-B | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3aa52e3-e1ba-37ce-9a12-2625d2b3a8d8 | -21.6595 | -43.989601 | 2024-10-07 00:24:39 | METOP-B | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4556deb0-cfb2-35df-80a0-87af9b2a0872 | -22.3736 | -48.563702 | 2024-10-07 00:24:42 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be3490bc-a303-3cdb-8bb9-c7a8cbb00961 | -22.3778 | -48.586899 | 2024-10-07 00:24:42 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42692e7b-7140-3364-ae96-40cff6ff94aa | -22.3757 | -48.575298 | 2024-10-07 00:24:42 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e82803c4-33db-3a9f-bd85-c44a92b22fbe | -22.2094 | -48.1646 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0c3d571a-d4df-3c9a-90d6-bbca4e388a7b | -22.195601 | -48.144798 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 967c24e3-0f73-399f-bbbb-800ef93459a0 | -22.197599 | -48.155701 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d9386696-fe08-383d-a965-a57f4cb89223 | -22.1996 | -48.166698 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a93bcc64-9f69-3591-85ff-1548cab141cc | -22.2054 | -48.1427 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a66121e4-6a9f-37bd-a7fb-22b6445fd6cb | -22.207399 | -48.153599 | 2024-10-07 00:24:44 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0120a9c7-eb7c-35eb-9b86-5f22544e841e | -21.496 | -45.680901 | 2024-10-07 00:24:48 | METOP-B | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 216f7107-0c39-30ac-8b38-450956f0e211 | -22.7209 | -53.1754 | 2024-10-07 00:24:49 | METOP-B | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84be0c18-d854-3b11-828b-cadb57463fa3 | -22.711201 | -53.177101 | 2024-10-07 00:24:50 | METOP-B | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ef82c30-4126-36d9-8acf-3c26051cefa9 | -22.7148 | -53.200298 | 2024-10-07 00:24:50 | METOP-B | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed8fc949-921e-3227-909c-7ba01b3192ee | -20.7449 | -42.850498 | 2024-10-07 00:24:50 | METOP-B | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 079eee36-c4f4-3dc9-b62c-a496f6bde067 | -21.6558 | -47.701698 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 794b19cf-3ce1-3245-b3d3-0e5e0bda324b | -21.6577 | -47.7118 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9368c3f4-7ce3-336b-92ca-7679f954edb5 | -21.659599 | -47.722 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0faa240b-7224-395d-abac-37f06c86e788 | -21.646 | -47.7038 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47813fc4-9150-3733-bbbc-640e8efe3206 | -21.6479 | -47.713902 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a0dca374-b60a-34eb-86d7-a26d2e064cff | -21.6362 | -47.705898 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82b05e37-1158-3cad-b8c2-9c2ed82f90b9 | -21.6381 | -47.716 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80b9be69-fffb-33ea-a9f7-55825f5edf9a | -21.626499 | -47.708 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ce61e1ed-c125-3827-917f-8e89ec250bc1 | -21.628401 | -47.718102 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 16d83b26-1bd0-38d4-af78-849405591df4 | -21.630301 | -47.728298 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aada444f-4012-30e4-94d4-263ab497da36 | -20.632401 | -42.901501 | 2024-10-07 00:24:52 | METOP-B | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23644520-3ff5-3c74-a071-27e62cd9ee91 | -21.616699 | -47.709999 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cea27859-adea-3da6-b384-18b80e57ffab | -21.618601 | -47.7201 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed09495-a94b-3dd2-8448-f07a41dc3986 | -21.605 | -47.702 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 32a78fa3-4cea-30f6-af05-522effde1a5a | -21.606899 | -47.712101 | 2024-10-07 00:24:52 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e31c4fce-bd81-39fa-b9e1-08ceef7f9432 | -21.5933 | -47.694 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1931e352-eef0-3315-bfb3-cefa2abe9628 | -21.5952 | -47.704102 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dd7163dd-c37c-3f51-b768-e321950bfafc | -21.597099 | -47.714199 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 93621dda-dce2-37e8-a1b9-d560f11203cf | -21.599001 | -47.7243 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2b96b180-e29d-3918-bf1a-62ceec47eedd | -21.583599 | -47.696098 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9e3f23-2cdf-37f8-a058-e367ff3a8e76 | -21.585501 | -47.7062 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 49825fd7-6e7e-3e5c-a444-d77773f1ff63 | -21.5874 | -47.716301 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e7fc9258-7ccf-37f3-8eb8-132aa08a8631 | -21.5893 | -47.726398 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5660db40-8b92-34f7-8404-1977165474b7 | -21.573799 | -47.6982 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 70df9bac-bcdc-330c-be5d-c5dc3d67871a | -21.575701 | -47.708302 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e0125b49-ab79-3b38-ad09-1a11f121868f | -21.5776 | -47.718399 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 72c54080-ff3c-38ba-8cb6-ba9bc4ffa13f | -21.5795 | -47.7285 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db133edf-98bf-3735-9bc7-21082de7af3f | -21.5814 | -47.738602 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb7d283-e1e0-30d4-961a-1230643b039a | -21.563999 | -47.700298 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7114a8-b2d4-32e6-8c7e-d7e35144d857 | -21.565901 | -47.7104 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e9a45a3c-b867-3acc-bbc2-1b63c8ad65ee | -21.567801 | -47.720501 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d64bd58e-52f6-3a6c-9a92-01f50e35a910 | -21.5697 | -47.730598 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90265479-30ea-39a7-a356-3d6af2ae3b4f | -21.5716 | -47.7407 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0134b383-daf0-35c6-9405-0070821198ac | -21.554199 | -47.7024 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9a274d6c-b3a7-3cda-a2ea-16c8385bb58c | -21.556101 | -47.712502 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ac966ade-bec1-31b5-a22a-fa0703cf5a8a | -21.558001 | -47.722599 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 057cf0a2-43c4-32e0-85e1-aaa7c1eb2a2f | -21.5599 | -47.7327 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cddeb3c0-d143-3c2d-9834-0334813289fc | -21.5618 | -47.742802 | 2024-10-07 00:24:53 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 08c5e0a3-6211-3442-968e-a04af2dba7d2 | -21.596701 | -47.9277 | 2024-10-07 00:24:53 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c66f1868-2e0b-3d0c-95cb-d557a5c061d3 | -21.5987 | -47.938099 | 2024-10-07 00:24:53 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9e5f855-ca2e-3819-9bd6-2aae1e052015 | -21.584999 | -47.9193 | 2024-10-07 00:24:53 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 100131f8-6724-3eaa-af1a-48a49b8fa25e | -21.586901 | -47.929699 | 2024-10-07 00:24:53 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eaed7365-d2da-39f9-8af3-7c2a7f7788d9 | -21.5889 | -47.940102 | 2024-10-07 00:24:53 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d0892233-6b1a-385e-80fd-1641f4f8ef29 | -21.590799 | -47.9505 | 2024-10-07 00:24:53 | METOP-B | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ceadfb58-cfeb-37a8-afe8-92551d6fbc01 | -21.1439 | -45.812099 | 2024-10-07 00:24:54 | METOP-B | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10a88e74-b182-3df2-8949-1a3d57ed5986 | -21.1455 | -45.820301 | 2024-10-07 00:24:54 | METOP-B | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 968b5fae-b168-3a41-8a79-4543b8696e8c | -21.5366 | -47.716599 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14f3b6f9-06e2-3d5b-8355-f44f66fcffde | -21.5385 | -47.7267 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec83965-2f59-39b0-bf8e-c232b5d2bb86 | -21.5404 | -47.736801 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ee4f6e12-73b4-3ad9-bdc7-85fc46880061 | -21.5732 | -47.910999 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 60054cd7-2343-30a6-bfa0-51095adabdfc | -21.575199 | -47.921398 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57ce3c0a-3390-3bc8-80f0-9660366455e3 | -21.5268 | -47.7187 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c7b1e7b5-f7f3-3b04-90c0-7de56f567509 | -21.5287 | -47.728802 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47bea8d5-4ff8-39c5-8cd4-9e556376f02f | -21.5306 | -47.738899 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
