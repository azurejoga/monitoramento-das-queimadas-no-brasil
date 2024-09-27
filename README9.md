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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d2fe999-4024-35d3-8e00-8245ca45bb5a | -12.7236 | -45.559502 | 2024-09-27 00:33:43 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2915a7f7-ce16-34b6-b443-adeb7e6289d9 | -13.5715 | -50.686401 | 2024-09-27 00:33:47 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66e7a76d-165a-3e72-9195-04ce5e66627e | -13.5734 | -50.695499 | 2024-09-27 00:33:47 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81e902a2-87b1-3b03-9058-955cc9f27a24 | -13.1554 | -48.522999 | 2024-09-27 00:33:47 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da1e67c3-746e-3f33-a08d-acf11d08ef68 | -13.1456 | -48.5252 | 2024-09-27 00:33:47 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b26dcec-0e17-38b7-80c7-05516e396c1b | -13.1472 | -48.5326 | 2024-09-27 00:33:47 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0645f31-3d7d-34ca-ba12-d62d25c67436 | -13.1488 | -48.540001 | 2024-09-27 00:33:47 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1557fcec-d8ce-3fdd-8a12-d078ac1e135a | -12.2315 | -45.482498 | 2024-09-27 00:33:51 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96214300-9f87-3ca0-bb87-4119da668489 | -12.2413 | -45.480202 | 2024-09-27 00:33:51 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d66e7211-5d65-3c59-99ff-608fe8e9492a | -12.243 | -45.487598 | 2024-09-27 00:33:51 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8e5e1f-fe0a-3c83-b04c-3cb84797fbb3 | -12.6587 | -47.893799 | 2024-09-27 00:33:53 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57d5375f-e4cf-3be2-b120-99339d5f6cfe | -11.4884 | -43.229801 | 2024-09-27 00:33:54 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b55f07e6-33fb-38ff-a09c-d8d2a36af25e | -11.4907 | -43.239201 | 2024-09-27 00:33:54 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 48ca37ae-ab12-3191-9c15-c27c8c092cab | -11.4786 | -43.232201 | 2024-09-27 00:33:54 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18f4db8a-138a-3906-b36e-aae1620c77f9 | -11.4809 | -43.241501 | 2024-09-27 00:33:54 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 58a4ec42-4d4d-3ecd-a7bc-b280aa96c1ab | -12.6206 | -48.284302 | 2024-09-27 00:33:55 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83ec2cb1-8a7a-309a-9e35-a9d33a69a4a8 | -13.2158 | -51.240898 | 2024-09-27 00:33:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d33face4-d6de-3642-ac2e-9c3211ddbc86 | -13.2178 | -51.2505 | 2024-09-27 00:33:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd57befd-be05-306f-9024-b86d788fe747 | -13.2197 | -51.260201 | 2024-09-27 00:33:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6a2defb-a8e5-38c1-8e89-508edd3c19f6 | -13.1824 | -51.227901 | 2024-09-27 00:33:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 568acc8a-2e94-307b-ac88-e1224005693d | -13.1844 | -51.237499 | 2024-09-27 00:33:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97f700c6-a3cc-30d3-af25-ce0225aee35c | -13.1726 | -51.2299 | 2024-09-27 00:33:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5990d4-1ba4-3fed-b628-17302fdb7a09 | -12.4673 | -47.959301 | 2024-09-27 00:33:56 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf4be87a-bebe-32c3-a818-c58a89d828db | -12.4689 | -47.9664 | 2024-09-27 00:33:56 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee40ac1c-cc56-361a-a079-0ffc31c5c9d5 | -13.1608 | -51.222401 | 2024-09-27 00:33:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21c4780d-fadc-3e9d-9db8-3b2a8686184f | -12.4575 | -47.961498 | 2024-09-27 00:33:56 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96e3c537-84b9-317c-a0a1-99af02e3760e | -12.1757 | -46.7374 | 2024-09-27 00:33:56 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f528e5e-a25b-3e65-84b9-616119439676 | -12.1773 | -46.7444 | 2024-09-27 00:33:56 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ef2d8c3-1091-3296-984f-dfc6c1d28acd | -12.4943 | -48.601299 | 2024-09-27 00:33:58 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3094723-5fd3-3890-8e43-9222c28f814c | -12.4959 | -48.6087 | 2024-09-27 00:33:58 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5799bd8-9221-33a1-9d28-c9fa38f23fc1 | -14.0385 | -57.848999 | 2024-09-27 00:34:02 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 644bd3a2-364c-38eb-964f-dcc0208a27cc | -14.0434 | -57.876301 | 2024-09-27 00:34:02 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bddcad4-ef60-3638-8d4f-9c62c9f701eb | -14.0338 | -57.878101 | 2024-09-27 00:34:03 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c3db676-c54f-39bf-8bd1-4f8285cfb320 | -12.7517 | -51.318901 | 2024-09-27 00:34:03 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 571d8ab4-6d0c-349f-a993-65a1eeb6ba03 | -12.5366 | -50.628101 | 2024-09-27 00:34:04 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fdf34f8-a4a1-3b03-af92-4ec41630c2a8 | -12.4778 | -50.396999 | 2024-09-27 00:34:04 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 677a6475-b77f-341c-9432-e85fd5aa3053 | -12.4796 | -50.405602 | 2024-09-27 00:34:04 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98b25617-0d6a-30bc-a38e-ccd3ee12084f | -10.4847 | -42.488602 | 2024-09-27 00:34:08 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 062a05e8-523c-32b5-9957-20ab52a87918 | -10.4872 | -42.4991 | 2024-09-27 00:34:08 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| abf35ad0-36e5-3cb5-86d8-c78aa8aba080 | -11.1924 | -45.540001 | 2024-09-27 00:34:08 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d545bbe6-f63f-3dc3-8e27-b67adaa0b560 | -12.2687 | -50.522499 | 2024-09-27 00:34:08 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff4b4c8-ec49-301d-84e8-c43e232364ef | -11.2718 | -46.113098 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea6f6284-e729-3d5c-a11e-6ea0d39e39e2 | -11.2735 | -46.1203 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c29423c8-63a9-3086-a2a3-f8bc346baf9d | -11.2604 | -46.1082 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99357c9c-1ff4-36a0-9297-3300764cec4c | -11.262 | -46.115398 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2fc97bd-fac0-3310-8ebd-590f79c43c7b | -11.2507 | -46.1105 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da75daf6-aa41-343f-8d1e-e3f1ad663cc5 | -11.2523 | -46.117699 | 2024-09-27 00:34:09 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43327ed5-3cf3-3a3c-b4c0-27afa2712e82 | -10.8647 | -44.6147 | 2024-09-27 00:34:10 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 895ff87c-0d1a-381b-870c-9cb5f13a36f7 | -11.1886 | -46.018902 | 2024-09-27 00:34:10 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16fd2484-98b2-3eb5-a222-73c224923d3a | -11.1902 | -46.0261 | 2024-09-27 00:34:10 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 648c19bc-4e54-3745-bd7d-cf38ad24cd14 | -12.1969 | -50.765301 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf5caa9b-a92c-35dc-b4bf-d0c75c0f025c | -12.1987 | -50.774101 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12137ad5-97d1-347e-bac3-96d2889a019c | -12.2006 | -50.782902 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26ca7ad6-f2b6-3bfa-8c2a-7d852f720691 | -12.2024 | -50.791801 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb95ce4-dfdb-32f4-8cb3-82762fffe95b | -12.2043 | -50.800598 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3fba3d35-2cab-3e80-a99d-6758b538f96c | -12.8524 | -53.991901 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b792d3d2-d611-3341-9629-1dce2b19a6d7 | -12.8552 | -54.0061 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18edf47a-3d8a-3250-8a9c-2807c982d649 | -12.858 | -54.020401 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0aa7e3f-bda3-3b7a-a21c-1f620b614127 | -12.1871 | -50.767399 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac7382f9-1680-33ea-b0e0-6dfa461c9863 | -12.1889 | -50.776199 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 434d0910-6145-35fd-a0c0-080e3d7526fe | -12.1908 | -50.785 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e09a44f1-ee41-3042-95e9-ffa494380f38 | -12.1926 | -50.7939 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 972442be-a9e4-3205-a8d7-7838356ce743 | -12.1945 | -50.8027 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0ad10e5-acdb-358e-9e63-2c8d409e02b0 | -12.2001 | -50.8293 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dce7bbe6-62d3-342a-a265-bd15fa346dcd | -12.2019 | -50.8382 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51e58cb0-6df6-3c1d-a9be-823c00c58612 | -12.8427 | -53.9939 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23fa5a70-31a6-321f-bd8d-7ca004a1847a | -12.8455 | -54.008099 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 884b26f1-43e5-35f7-8ef6-ad62c8c212c2 | -12.8483 | -54.0224 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a331129-9c5b-391a-8e9d-89a67f6d00bd | -12.8511 | -54.036701 | 2024-09-27 00:34:10 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42a54489-3eea-3119-ae99-98fa0fd3d1d9 | -12.1773 | -50.769501 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba6264a9-20ff-3fa9-92c3-880a62f4f213 | -12.1791 | -50.778301 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8638876f-9f96-3704-97a3-5652be35992e | -12.181 | -50.787102 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb6897f-9f3c-37a3-8ab1-3b92716115c7 | -12.1865 | -50.813599 | 2024-09-27 00:34:10 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5f35c6-70af-3cec-b09a-31d3f9fd03de | -10.5548 | -43.603298 | 2024-09-27 00:34:11 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc338b5b-b6cd-3242-9a7a-ebbfe2f815e3 | -10.5526 | -43.5942 | 2024-09-27 00:34:11 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1b14e5a-9073-3c3d-afc4-391990556b16 | -12.8204 | -53.983601 | 2024-09-27 00:34:11 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 434cc659-616e-34b9-bb65-370e8fff01f5 | -11.5222 | -47.825298 | 2024-09-27 00:34:11 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 502a52dc-dde2-3032-aaa9-7ac2fd7c16e4 | -11.5238 | -47.832298 | 2024-09-27 00:34:11 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7566cef6-71b5-3eea-b80e-7c8cf6d2fd33 | -12.7869 | -54.019798 | 2024-09-27 00:34:11 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc1a730e-851d-3d02-8079-ac9b6c5c1462 | -12.7772 | -54.021801 | 2024-09-27 00:34:11 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fedf3ea1-46d7-378b-a91d-6261daeb73e0 | -10.9174 | -45.5103 | 2024-09-27 00:34:12 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28408787-2640-3c0e-a51d-846e07553afb | -11.0858 | -46.1563 | 2024-09-27 00:34:12 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af619fc0-4314-3ec2-a910-20aec21e0757 | -11.0875 | -46.163502 | 2024-09-27 00:34:12 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcaf9c27-fafd-3d7e-871a-85ff9d40c5e7 | -11.0891 | -46.1707 | 2024-09-27 00:34:12 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1779f21f-8420-3a79-af3a-c2bdbf46df8b | -11.0907 | -46.177799 | 2024-09-27 00:34:12 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfa086c-6ee0-3f68-aea1-e140f40142d2 | -11.5825 | -48.426601 | 2024-09-27 00:34:12 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 721aee5d-733e-32ce-bae9-d03ec2d7ba81 | -11.8394 | -49.611198 | 2024-09-27 00:34:12 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44896e5b-92ff-3ec1-b28a-5369483a411f | -11.8411 | -49.6189 | 2024-09-27 00:34:12 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef4b9fc-a8dc-3425-a49c-3a863fb67bae | -11.8313 | -49.621101 | 2024-09-27 00:34:12 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f53ea5f-b7e3-3ebb-8a18-795918eefeaa | -11.8329 | -49.628899 | 2024-09-27 00:34:12 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57b3bd8b-537e-3e6a-b5a6-a33fb178ec30 | -12.5423 | -53.146099 | 2024-09-27 00:34:12 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05e1cf03-3706-386e-a459-9fa9f42d58d4 | -10.5883 | -44.271198 | 2024-09-27 00:34:13 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 871cd357-74b6-3acc-a24c-049a9a5ec745 | -10.5903 | -44.279598 | 2024-09-27 00:34:13 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0ec770-009f-3e58-803a-1459b4a813e4 | -12.5326 | -53.148102 | 2024-09-27 00:34:13 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8630522e-42f3-3341-9d74-7c7aa1367912 | -12.535 | -53.1605 | 2024-09-27 00:34:13 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fda6db57-c84b-3a6c-ad12-521e422759e2 | -12.6991 | -54.037498 | 2024-09-27 00:34:13 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e05c2b0d-3f6c-3e21-b39a-965a3259e5d6 | -12.7019 | -54.051701 | 2024-09-27 00:34:13 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cac5271-09ce-386c-bb16-9dec89b0c741 | -12.547 | -53.474602 | 2024-09-27 00:34:13 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caa9effd-4960-3ce9-871b-e6df44b0706f | -12.5495 | -53.487598 | 2024-09-27 00:34:13 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce2d4ad-5673-3852-9859-e4bce75c9e85 | -10.723 | -45.2048 | 2024-09-27 00:34:14 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
