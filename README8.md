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
| 23b47f6f-8747-3c62-a27c-022cf3eaec37 | -10.89928 | -45.56587 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc3920c-42e9-3c9c-bdee-2ec4f0a2e424 | -14.18009 | -46.15559 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d10bb912-cfc4-3b92-b5a1-f22f29e3dcf9 | -14.17607 | -46.16036 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7523b259-f7f0-30ee-aada-e71dbc4bba4b | -12.10162 | -44.86337 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d71cc223-5bc5-3f50-8917-6985824fcaad | -14.63107 | -46.3723 | 2025-09-14 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 56251c6d-2348-30ba-9ef4-4a563772a261 | -11.45766 | -43.57428 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d73aaf6e-48ab-3b3e-a839-912cdca63b9f | -14.63235 | -46.36651 | 2025-09-14 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c40517a-34dc-38b7-b73a-509dc9732e14 | -10.7701 | -44.78794 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06618bba-1479-3c2f-80dd-db78ab1816c4 | -11.44611 | -43.56639 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b8da63-0424-391b-a66a-88a09a79a358 | -13.28667 | -43.79352 | 2025-09-14 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cfbbe35-8af9-312d-aba3-3921ae1e3e14 | -11.46296 | -43.5806 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01345f15-d610-3679-b454-37c845821bf6 | -11.50459 | -43.64275 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9ad6b4c-ba53-3a1c-89e5-4f12a5ecc050 | -13.93337 | -44.82595 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e95d0be5-6dad-3944-9c29-347a5ab4f90b | -16.8398 | -40.84946 | 2025-09-14 03:28:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 22710fb8-6b9f-3b2a-b513-71b8e3272b48 | -14.18988 | -46.16407 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b091e69-cf06-3f99-95b6-b5cb6c873616 | -11.35137 | -43.50295 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e268ec7-447c-3d56-b13c-11c24419d577 | -12.61561 | -44.20597 | 2025-09-14 03:28:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47debef1-3a87-348f-aec5-aa26cd52b987 | -13.9423 | -44.81612 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef084edb-7a1b-35a2-8af5-aad021b6684d | -14.15721 | -46.2446 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dc13167-5ee1-3956-a31b-a0477b234f3f | -14.40865 | -43.23979 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 123fd465-8988-39f0-877b-cf761b87e040 | -12.61671 | -44.20062 | 2025-09-14 03:28:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9717d0c-ed1a-3c2f-8539-561d6f2dd22c | -14.76102 | -45.2751 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea855b03-b53d-3848-8068-bfc822ed6dcb | -12.10123 | -44.85848 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82571074-681e-3afc-8014-429023b37cba | -13.92839 | -44.84899 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f84620e-25ff-3ae5-8205-129b6e499641 | -13.93513 | -44.85564 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07594e37-e223-35c0-9b1e-af329dc78c1e | -14.28348 | -45.10761 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c45284bf-dba1-3276-bcc1-f2e2934c920d | -15.434 | -47.356 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41123832-69fc-3e48-a83f-107973cdf3e1 | -13.93878 | -44.83817 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fbd23ae-8802-3791-a3fa-dc6fd96513ea | -16.83487 | -40.84899 | 2025-09-14 03:28:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2de4046-c618-3521-885a-fc2a24d6c706 | -14.43252 | -43.21316 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 498b9b86-e3c9-3b8d-bd92-3ace461acb73 | -15.47979 | -47.32317 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d692e170-1154-30ba-9b53-46694cbc2b94 | -13.93088 | -44.83747 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bb635b4-c203-3dc9-9590-838e37dd4cfd | -10.76324 | -44.78656 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 593e2cc2-4d26-3ffc-b905-e41e3fbd737e | -17.5919 | -42.7341 | 2025-09-14 03:28:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1c64788-c148-3bd1-ab1e-38a7aa2cbc2a | -17.69039 | -42.5576 | 2025-09-14 03:28:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4139e3e5-638e-3563-b16d-3ce5c44033f7 | -15.63886 | -44.37603 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8286951c-3c69-37fc-88f7-6d3eba4b0238 | -17.38957 | -42.62831 | 2025-09-14 03:28:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6273594-8056-36df-81fb-b1a5cbabba02 | -13.29002 | -43.78756 | 2025-09-14 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ea7ba0-a631-3073-8b65-a61ff616bded | -16.91264 | -41.28627 | 2025-09-14 03:28:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 165ed5ff-9d28-3304-8522-5abfa46e15d4 | -17.69417 | -42.56603 | 2025-09-14 03:28:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0f74b0db-b8d6-3a1c-93f3-71765c66fd14 | -10.599 | -44.33889 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0241ab5e-25d3-35fa-a8b2-78af306e2bda | -14.43926 | -43.21012 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 169e521d-836b-3a0c-8b8c-42cb8636f41e | -14.19247 | -46.16594 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37176ca8-8a05-38a2-8055-971b3ca0ca8c | -11.49825 | -43.64147 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d4cb582-95bf-3b59-948c-c3fc80782ab3 | -14.17864 | -46.16232 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd8d1647-9e4e-3754-8cf4-540d9dc86f69 | -13.92744 | -44.85983 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b0cad49-e31f-3792-bc4c-686e12ae912e | -13.92989 | -44.84815 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6171f74-b3e3-373a-90c5-373d3e4829c1 | -10.75783 | -44.77818 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7b55fd5-cf48-3b85-babb-5001579bb0ab | -13.38978 | -41.39785 | 2025-09-14 03:28:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d87f7c9d-8666-375b-90c5-c6b14086828d | -10.77146 | -44.78125 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ea490cc-5fb8-3d3d-b2a9-2ea5e800d87b | -17.58981 | -42.73404 | 2025-09-14 03:28:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85cb153f-e151-3e5a-83a7-2b030d16927f | -14.40957 | -43.23536 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1130d6-f4a9-3268-a30e-6cd7595dd787 | -13.93754 | -44.84407 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33558d5d-9dbd-3a5d-9d48-724e9d1a321c | -10.76465 | -44.7797 | 2025-09-14 03:28:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83a4d78c-ceab-3526-8b64-a627e785bd75 | -11.13323 | -45.32817 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a958c8e-d454-36df-894a-4057042451f3 | -13.92586 | -44.86069 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8ddcb2c-d4f5-3be4-b4e9-fcb4232955c6 | -16.91307 | -41.2859 | 2025-09-14 03:28:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cdc75b58-0d32-37e4-b25c-a4e1f8e95d5e | -14.15546 | -46.25245 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 970357df-9800-3728-8212-582190282d68 | -17.39149 | -42.63006 | 2025-09-14 03:28:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c538047-17ad-31b2-88d6-6de346c45560 | -14.17756 | -46.15369 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa123a1a-5471-3405-aaf2-4ba0b43a2612 | -11.24258 | -44.77549 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba5dd530-aee7-3a11-ae14-125d180696d8 | -15.63166 | -44.37953 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0154fb0-4200-31a4-886e-2a5036cb259e | -12.08781 | -44.73081 | 2025-09-14 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ca63569-de2e-30c1-b033-01f315599bd3 | -11.24936 | -44.77696 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1326fb32-2dd1-3b28-9e31-0d42871c95fb | -13.94003 | -44.83217 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baa51295-2c1c-3323-abbb-6011487ffc63 | -13.9324 | -44.862 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da27d412-9c6e-34cf-8def-512c81936db2 | -14.16539 | -46.15597 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27780984-b440-353d-85c1-a4a265247c51 | -13.93734 | -44.8391 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3524d06-ee46-3664-a86e-182968417405 | -10.89785 | -45.57272 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 043ef8b6-fbec-36cb-a02d-6a9b56ac89fa | -12.08644 | -44.73726 | 2025-09-14 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7554a643-fc2a-3aa8-90a9-402393748bd5 | -11.14157 | -45.32336 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fedad75-3730-3298-9245-ed1a105aa667 | -16.50187 | -42.12672 | 2025-09-14 03:28:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 517824c4-aa96-3f33-88c1-fbd1ad7d0a66 | -13.93483 | -44.85072 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5233be5-9525-376f-a8be-f7dc45166aa1 | -14.18553 | -46.16424 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4651232e-fda6-3ada-9c13-09a036086676 | -13.28771 | -43.78857 | 2025-09-14 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f0c480-5b5b-35f5-8e73-c551a7db2286 | -11.35239 | -43.4979 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55e4ea1a-42e0-3918-9a9a-9e95f131baac | -17.59114 | -42.73764 | 2025-09-14 03:28:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b1d68d1-de27-3b63-b97d-eb8d77969889 | -11.25063 | -44.77091 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8580c53-598d-3eb0-96ee-17d9bfd09e6b | -13.93457 | -44.82038 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db83a011-1fbd-3bef-a1ed-023e4a7fd88d | -17.68965 | -42.56116 | 2025-09-14 03:28:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 90431395-4ba1-3e8e-ba72-67a802b33352 | -11.43981 | -43.56503 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3490596c-bb07-36f4-8ba1-de171ede65c3 | -17.58577 | -42.73653 | 2025-09-14 03:28:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bb93211-0aa6-3b7b-8bbf-fafcea5c2bc6 | -15.63433 | -44.37673 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac42dca3-c40a-35e2-b42b-9a8f37289b54 | -14.20717 | -46.33682 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a63e86e-16cd-3750-b042-d889b0734e4e | -14.44103 | -43.20149 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eba91d7-db95-3ae7-9a4c-bc64074aa8ec | -16.50125 | -42.12974 | 2025-09-14 03:28:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3857f1a-4208-31a5-a154-190237e8ef13 | -13.93589 | -44.81943 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c592bf43-a0b4-39ce-b338-8981d4a5ea7b | -14.15378 | -46.25994 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49526049-f6c1-3fc2-b231-779a5f056197 | -12.12705 | -44.84257 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e602614a-b306-371e-9185-a280bdf63584 | -17.38884 | -42.63185 | 2025-09-14 03:28:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| caa00c61-2585-34e7-8c62-8725299d963c | -14.63042 | -46.36291 | 2025-09-14 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3919b469-31d9-3848-89de-c640de130050 | -14.43431 | -43.20446 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6510456b-d4cf-34f5-9c58-3a05206a76a7 | -17.94499 | -42.83901 | 2025-09-14 03:28:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff3ea34c-c579-3b2b-9f47-082c99c31070 | -14.28462 | -45.10228 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b0bed32-0271-3236-bcaa-89a346d5c3b8 | -15.63329 | -44.38168 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd08b870-5d93-3e51-b945-37485a0139c0 | -15.79935 | -43.38385 | 2025-09-14 03:28:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4b07bc8-f09d-3e02-a411-e316a85dff12 | -12.1202 | -44.84185 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc5ceb02-a554-32a7-843b-4bc39259b656 | -14.20242 | -46.33959 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8899c0f-f669-3a3d-a2bf-7e6e518dd071 | -17.39224 | -42.62653 | 2025-09-14 03:28:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 177ba973-b6af-38cd-b609-52327386d98b | -14.15854 | -46.2549 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README9.md)
