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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b7d3531-2585-3799-87fa-845adeae760a | -22.75545 | -52.19484 | 2025-10-24 04:21:00 | NPP-375D | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a6708f24-d0c1-3365-9eb3-7fcc2fcbd792 | -20.55986 | -54.65462 | 2025-10-24 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e499429-a73e-3135-a8fd-9804b896d0e0 | -24.76649 | -50.96409 | 2025-10-24 04:21:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ef53ffd-a943-3fa1-aa5a-b5b56def3b07 | -21.61911 | -45.42134 | 2025-10-24 04:21:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 98098c8d-8165-398b-a5c6-0ec12e21e475 | -20.83356 | -45.84079 | 2025-10-24 04:21:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8223c360-0717-3e84-8ec3-5cbec4447384 | -22.97681 | -47.39637 | 2025-10-24 04:21:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 25104bd8-bf81-39a2-aa42-0da0e36da792 | -26.34391 | -52.31973 | 2025-10-24 04:21:00 | NPP-375D | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 501dd277-aa99-3788-be67-3cdac304707f | -24.77012 | -50.96476 | 2025-10-24 04:21:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bdebb715-5caf-326c-b454-8a4e2549994e | -22.13965 | -45.64475 | 2025-10-24 04:21:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a5dfe4b-509e-35eb-8eb6-8a39c679e3ec | -22.38972 | -53.53064 | 2025-10-24 04:21:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f9f8bb6d-0cec-3999-ae21-62111acfe6ea | -22.75651 | -52.18931 | 2025-10-24 04:21:00 | NPP-375D | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 03b32153-9cbf-3bc8-888b-f7a2fdfcb58c | -21.12698 | -45.72793 | 2025-10-24 04:21:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f6f63ed-e163-33e5-8ff1-cb5f1f3c0d9e | -20.57905 | -45.88919 | 2025-10-24 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76c9db28-f674-39dc-b42b-4c2cb8e0f620 | -24.12799 | -50.76354 | 2025-10-24 04:21:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 683d6ebf-5376-33ca-bde0-0b653014aadd | -22.14022 | -45.64095 | 2025-10-24 04:21:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1fabe4cf-b454-3454-adb6-8504d9197af9 | -22.98014 | -47.39699 | 2025-10-24 04:21:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1b5c715-3c16-3df8-ab44-e0ce86cf88a9 | -21.76152 | -52.27053 | 2025-10-24 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e418f1cc-4f8f-3822-81fc-be15ad6c8248 | -21.20242 | -48.69828 | 2025-10-24 04:21:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1407082a-e1b4-337d-9a2c-edbe9b751114 | -23.9769 | -49.64798 | 2025-10-24 04:21:00 | NPP-375D | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 47ec886d-67b9-3761-b808-788f9c942137 | -20.50106 | -54.59933 | 2025-10-24 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed2cdc5c-0eee-3a75-ac27-934cdad0d293 | -26.10347 | -50.34996 | 2025-10-24 04:21:00 | NPP-375D | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6cefc73b-5559-35b3-80a1-d481b34d4248 | -21.17834 | -46.40689 | 2025-10-24 04:21:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0263f5b5-69e4-34a9-8c21-4b1a3899c535 | -21.76225 | -52.26673 | 2025-10-24 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1e4013f8-c5b9-39fb-8c9f-dfca50cc94a5 | -21.14626 | -50.46721 | 2025-10-24 04:21:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0cb6dff9-0a15-3224-8d9c-239ef21be1ed | -22.89249 | -47.74929 | 2025-10-24 04:21:00 | NPP-375D | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1848f623-5682-34ca-aed4-02c3c3bd87a5 | -22.28489 | -46.82951 | 2025-10-24 04:21:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9e60caa-397c-3665-99ee-c5edd5456578 | -21.12641 | -45.73168 | 2025-10-24 04:21:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bd65c256-8e89-3070-bd06-7fe775e46889 | -24.52196 | -51.45798 | 2025-10-24 04:21:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e02bc09e-58c0-3960-afce-b07ea51de939 | -21.61574 | -45.42075 | 2025-10-24 04:21:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f467ecac-1b56-3941-a3c3-869138a8440c | -20.92529 | -55.77452 | 2025-10-24 04:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4bb9a8c-349e-3657-8562-2d0603a1f211 | -22.3906 | -53.5262 | 2025-10-24 04:21:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f8b01e83-4b35-36c1-a23e-1f861cb56955 | -25.03928 | -52.56306 | 2025-10-24 04:21:00 | NPP-375D | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4e9924ec-b1d6-3b75-9f42-cca40eff78c0 | -20.58238 | -45.88979 | 2025-10-24 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c42a2c8b-a0ab-3504-a573-43195cbddfc6 | -23.34879 | -50.40516 | 2025-10-24 04:21:00 | NPP-375D | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a7c620a9-1e3f-33b0-bb56-2fb5f1539f80 | -24.12718 | -50.76804 | 2025-10-24 04:21:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b52161c3-8f05-325c-85f0-71061b0c3357 | -21.13033 | -45.72851 | 2025-10-24 04:21:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b9ae3ab-09c8-3faa-bab5-bef5e06481cf | -27.15696 | -51.28985 | 2025-10-24 04:21:00 | NPP-375D | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6df02d46-a8dd-3f27-b33d-db06276c22a8 | -24.51826 | -51.45718 | 2025-10-24 04:21:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ca3caba4-6ef6-3d21-a09b-dc16b720994e | -23.34779 | -47.16901 | 2025-10-24 04:21:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1eab2b1e-7906-35ef-83fa-7f1909c0feac | -20.5587 | -54.66028 | 2025-10-24 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6476e55-ab94-32db-bd82-0161aed0eb24 | -20.49776 | -54.59705 | 2025-10-24 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed434a68-6f4a-39a8-9828-569d7ce5dca9 | -20.6524 | -55.08588 | 2025-10-24 04:21:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a13bff88-4b9d-33d8-8364-c7bb65fe7a04 | -22.2843 | -46.83324 | 2025-10-24 04:21:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fca5cf0-256b-3082-b4e7-88a4cb50e5d1 | -24.18481 | -51.68656 | 2025-10-24 04:21:00 | NPP-375D | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96cee950-c4f6-3f54-9938-162024a78f9d | -23.38274 | -46.41419 | 2025-10-24 04:21:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 93d5835d-8e56-3974-ba00-a2ebf529ac58 | -23.34506 | -47.16462 | 2025-10-24 04:21:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29bf458d-ef2c-38c4-a1e9-44c2a16bb507 | -24.42031 | -50.76355 | 2025-10-24 04:21:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37c3e3cd-8175-3aaa-a335-fccaeb21cc28 | -23.1664 | -46.92416 | 2025-10-24 04:21:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13423052-1b35-3858-9596-b6080d0181b5 | -23.1703 | -46.72362 | 2025-10-24 04:21:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 786dd24c-38c8-3d3b-8ef9-7687fb6fe963 | -24.52734 | -51.42895 | 2025-10-24 04:21:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0969dde7-dbe2-37fd-9c3d-fecd45cf094c | -20.44143 | -46.59321 | 2025-10-24 04:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 169bd305-6bfd-3b08-aad7-d9391d2f5534 | -24.12357 | -50.76729 | 2025-10-24 04:21:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 63dd7c3c-1565-30ca-bfe9-cfd4c8bd627c | -20.49662 | -54.60268 | 2025-10-24 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4897e6b6-8280-32bb-9762-c54cb12d3811 | -20.7084 | -46.2723 | 2025-10-24 04:21:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8696534b-a121-33aa-a62f-2d0dfed2afa4 | -20.92597 | -55.77137 | 2025-10-24 04:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f46595a-c7b4-366d-8b54-193643972b79 | -22.89311 | -47.74551 | 2025-10-24 04:21:00 | NPP-375D | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5bdda423-9a7e-34bc-bba5-e696027aeae8 | -26.10272 | -50.35419 | 2025-10-24 04:21:00 | NPP-375D | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a368e37-3299-3713-b843-3ddbf3d65601 | -20.43811 | -46.59261 | 2025-10-24 04:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cd47d80-a805-34cd-9964-774fdc46b024 | -21.19899 | -48.69759 | 2025-10-24 04:21:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94cb58eb-cb57-3bbd-9e43-62e116ba8f99 | -28.61864 | -50.62516 | 2025-10-24 04:23:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32e5368d-e703-33c8-972c-3191914266fe | -28.62206 | -50.62592 | 2025-10-24 04:23:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9819230b-d318-35ff-b33a-74008f1c43ee | -28.70115 | -50.20457 | 2025-10-24 04:23:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dc9c287-23aa-3963-affb-d4cfce41c78d | -29.23399 | -49.67901 | 2025-10-24 04:23:00 | NPP-375D | PASSO DE TORRES | SANTA CATARINA | Brasil | 4212254 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d6cbf29c-6d27-358f-9b49-2c26846bf821 | -28.22664 | -50.35905 | 2025-10-24 04:23:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5fb9b699-9209-3d66-ae45-f6c9d66946bc | -27.69844 | -52.56428 | 2025-10-24 04:23:00 | NPP-375D | CAMPINAS DO SUL | RIO GRANDE DO SUL | Brasil | 4303806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b46d1759-bc8e-3121-8d09-dad9d039fa8c | -28.87942 | -50.63626 | 2025-10-24 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 191ce679-cfd7-3092-94fe-d6369c3193eb | -28.7226 | -49.11049 | 2025-10-24 04:23:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f874e7e3-28a8-3616-ac77-3876b15a4bc3 | -28.72324 | -49.10653 | 2025-10-24 04:23:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfd9c8d7-34dc-3b88-9c7f-c8d752538802 | -28.22324 | -50.3583 | 2025-10-24 04:23:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 059e627b-ed27-314e-bab6-c0450ad4131f | -9.6061 | -46.9099 | 2025-10-24 04:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5d0f6c87-d9bb-3893-a237-4b0d64735cf6 | -1.59524 | -54.30742 | 2025-10-24 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e69d2979-ce9c-3b08-9a8c-10b381e0fbf5 | -1.54148 | -55.40337 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b788c72-c7de-3c6d-bfa8-d2e0e1b6965a | -2.42594 | -49.27701 | 2025-10-24 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69572177-d411-3dc6-a492-d25181612c73 | -2.44464 | -47.15648 | 2025-10-24 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ff168af-470a-369d-bbc2-8a39fa89d8b9 | 0.41291 | -51.08509 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 622918c7-9723-3b5a-922a-6a1031e5849d | 1.64435 | -55.75635 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d50f4c5-5b3d-3602-babd-925ea446faad | 0.11324 | -51.36758 | 2025-10-24 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae534cf-515c-3163-b850-c353eef9590a | -2.41931 | -48.43801 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d48701e4-784b-37f7-b312-bfd8250c235c | -2.80823 | -48.6651 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aedc7db0-2dae-3f02-a0a3-80d45de399b1 | -2.47052 | -49.23082 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed1efe17-f3c9-3cfe-910b-b867e244cf52 | 0.10587 | -51.36872 | 2025-10-24 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be437b93-4a36-3ac0-b112-ce22692c9954 | -1.5407 | -55.40824 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74c27ec2-541e-346d-9093-f9c825aa266b | -2.30298 | -48.57119 | 2025-10-24 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1be3ac5a-a154-3893-866f-5bc99c8887bd | -2.42261 | -49.27649 | 2025-10-24 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad6476c0-4578-3eba-9b7f-960adb37793f | -1.54927 | -55.41459 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4cf9d1d1-b990-3e0f-b8a0-8c205f83958b | -1.21056 | -53.79044 | 2025-10-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99f212c6-74ba-35d4-bafa-985f9aee8731 | -1.92647 | -52.14529 | 2025-10-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd9e547-c9f1-3845-8272-6909c0a41383 | -2.42261 | -48.43852 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a229486-b408-3950-8a3b-5eeef602343c | -1.13468 | -48.84662 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3bb81ef-5386-3879-b5f7-114bbc01732b | 1.66367 | -55.71459 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc7d9294-6c8c-3c71-a0c8-462a369ef802 | 1.35719 | -50.70371 | 2025-10-24 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa684afc-8621-311d-ab24-7e2fafe03d61 | 1.64568 | -55.7651 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7eb2ce3-bd2c-37ae-92f6-5147055a4a20 | 0.36015 | -50.93904 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d592d95b-f0da-372b-a0c5-73bc788061a0 | -2.87144 | -45.25935 | 2025-10-24 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df70a52b-dc39-37dd-9d33-b0c509663e91 | -2.73948 | -47.13614 | 2025-10-24 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd891c01-3344-3421-87ae-baa3afe2b28d | -2.47384 | -49.23134 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ca61cde-2234-332e-9d28-2ffff64e55b7 | -2.26338 | -47.85381 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9ce4a069-0d6d-3a22-a2ce-9ed40451e1a5 | 2.07387 | -55.7181 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b84647e-1c69-38a4-816d-b54689d026cf | -2.42539 | -49.28049 | 2025-10-24 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01a9306e-be28-3321-865b-4cd2f5696d9b | 0.46494 | -51.00911 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
