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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99997599-4cf8-3b7d-add3-cc414d013d87 | -14.23144 | -51.92648 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddb67607-04fc-3321-a49e-cbefafc49b66 | -15.85971 | -56.08557 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fda1cb3c-1685-3b77-a91c-28aa9e1a59d7 | -16.50049 | -55.18252 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8833605e-3a78-30ed-96a9-edf4c18b94cb | -13.4385 | -57.07212 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d385c1c9-1b8d-3778-9237-509ac34c492c | -14.08159 | -58.81808 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8f49a96-94e3-3aee-8322-384876b988ef | -13.4396 | -57.06504 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3ca66c-7380-3903-8b55-4a0d91062c7c | -14.02013 | -53.66003 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 057b06ae-8c8d-313f-a929-73d0e3e8ae7d | -15.21388 | -52.80584 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84e6eeda-3969-300a-9bb4-45ee98c92939 | -15.86982 | -55.55465 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da72697c-ad72-307b-aa2a-8aa616d41758 | -15.54256 | -50.27632 | 2026-08-20 05:08:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4864e900-8940-3474-b4c5-62e1497c81e4 | -18.03476 | -44.62311 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 01b6d1f8-c508-376e-8a36-6166eb6002a8 | -14.2186 | -52.89196 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bf9d196-bfe6-3cb4-bdb4-02dd5b23c2bb | -14.22776 | -51.92193 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f353b8db-4385-344f-aa66-89927d712307 | -14.09108 | -54.00402 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdff291b-c082-35a8-9eea-152c8d0b0c12 | -14.51614 | -52.99815 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4c69029-629b-3b2b-98d2-4a015c3b54ec | -18.03539 | -44.61575 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 34.3 |
| c9296d25-ead2-3cff-869e-6dbae2208bf6 | -14.07096 | -58.82004 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca7ea5a4-c426-3e32-9306-28850fc37b54 | -17.9481 | -44.41373 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 095c22ce-91e9-3b35-b94f-0eb806bd1dc1 | -14.23195 | -51.92254 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6fa6d53-ed0f-3a6f-b1ff-3667e5f899c7 | -15.35985 | -52.77399 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8ef953c-9357-31a4-8057-eb03f80de8dd | -15.26858 | -56.48804 | 2026-08-20 05:08:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d0eac12-576e-319a-89b6-a61448388888 | -18.8512 | -47.1442 | 2026-08-20 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b870d021-ac52-3967-a35d-6f0b51e7bb61 | -19.39322 | -46.40704 | 2026-08-20 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cd96c09-482a-3732-bac4-2d205af38855 | -14.30666 | -51.91246 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 189eb12d-1d1c-32c2-85fc-4c6831d25430 | -21.87889 | -46.56974 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8833167a-285d-3160-9ff9-91d1b33729f4 | -14.29283 | -54.6853 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dac86e3-4a14-33c6-9970-f900fdfd33d4 | -15.36925 | -52.79665 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93de96f5-c423-3fc9-ba19-9398a41262cc | -14.32346 | -51.91508 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4351e95-272b-3be2-b669-bdd1a3c329ec | -16.08161 | -54.97771 | 2026-08-20 05:08:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9221da9-74b9-36ac-a833-cee055d8cb40 | -14.21538 | -52.886 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3402bf89-8432-3cee-99ec-1842f77db895 | -20.288 | -46.70887 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c86e2f1-9b27-3bc9-913d-66de8fc0973a | -14.54481 | -53.02317 | 2026-08-20 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f7738a2-38cb-3cf1-9e79-ae4b4756b111 | -15.36436 | -52.77095 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3434eb09-5597-3db8-b36e-62c083f08f68 | -13.43573 | -57.06804 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83a49a5-7d57-3573-9052-750352436d2c | -14.08435 | -58.82228 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb31c84b-8bb5-30a9-b3c9-9fd9b6c33f39 | -18.04179 | -44.62359 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 88cfd848-a219-31b1-8a40-c383dd0a59d0 | -14.07824 | -58.81752 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cbb8ec3-cd54-37bd-9c63-e661c1e949af | -14.22724 | -51.92588 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d776c78-1ccc-3f99-a36d-e65f52cd07c5 | -13.44014 | -57.06149 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 441b72e4-42e3-3eca-90b7-9a375dc09319 | -20.27659 | -46.73534 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a8940849-46d2-35a9-bef1-8ee43df48543 | -14.27925 | -51.88887 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f5edef6-565f-3d18-a6c0-9798fd4462e7 | -13.44251 | -57.06885 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bffcc24-c79f-3e8c-a751-293bf1af9c87 | -14.01755 | -53.67838 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 144be1ab-0a3c-3bfa-ac72-f1e4fa858a42 | -21.87193 | -46.57478 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| eb6fc9ff-bd8b-37ce-aeff-6b0b3083c1ce | -15.35873 | -52.77489 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea07b27b-3c13-35f7-b562-ef37d7828ac8 | -14.20674 | -52.89046 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46ac60f9-14f0-3659-9618-8b7cd8eb55f5 | -18.00039 | -49.4014 | 2026-08-20 05:08:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a408a67-8dce-3165-b29e-fb16ed51014e | -15.21742 | -52.80994 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb134702-f6f2-3878-b5d0-c93fc2a85fe2 | -13.74514 | -57.61508 | 2026-08-20 05:08:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b40935-04dc-3a34-9054-52bc1bcd7a36 | -20.26314 | -46.74292 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d6e3db2-47d3-3592-b8df-7f0b925e1ca5 | -16.07862 | -54.97285 | 2026-08-20 05:08:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8706d46c-ce1d-3b2b-9e7a-556b94d11451 | -15.36495 | -52.73439 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ff9d466-c166-379d-b552-1bdff3fcf826 | -15.36347 | -52.77783 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00224129-d277-3be9-9227-3b241add35bc | -13.44474 | -57.07647 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c759835-5913-342b-b130-608bb0779559 | -20.27961 | -46.7332 | 2026-08-20 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b68b0a81-2b96-34a4-96c2-252dc00d7371 | -14.22182 | -52.89784 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46a588e2-9795-354f-8673-a810e4286651 | -16.06905 | -54.96254 | 2026-08-20 05:08:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93de5924-a646-38aa-95ba-18b9827da813 | -16.50407 | -55.18302 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7aa3d7b0-66e1-30ee-8b97-1743cbbcf52d | -21.87875 | -46.56877 | 2026-08-20 05:08:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8ee12372-fb76-3c6b-8005-1dd29eb2358e | -18.5582 | -48.29327 | 2026-08-20 05:08:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d4c9d360-3b82-3566-a8a8-910b714163fa | -14.01947 | -53.66472 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fafa3577-1a1e-378f-9ee8-7e55b86f7455 | -15.88504 | -55.57301 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c130a5bc-4687-3675-8e36-0a02d60f7ec6 | -20.32382 | -47.74589 | 2026-08-20 05:08:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72980450-9e3f-32af-be76-1c409aac154f | -14.1545 | -52.95092 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d3cfc13-077a-3c14-990a-05d042f1816b | -15.36947 | -52.73133 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46dd8f8d-d50f-3b72-ae79-365c622c4504 | -16.07802 | -54.97715 | 2026-08-20 05:08:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d427f443-d5dd-31c8-a0d3-68dc2d8846bb | -14.08493 | -58.81865 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed81f2b-99ed-37b8-99b8-95e3e109e172 | -14.25874 | -51.81669 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09378242-4bf7-3a1e-8a3a-274a5f6211ee | -15.35941 | -52.77741 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c41491d9-dfb5-38e6-8731-18e17547fb46 | -13.44583 | -57.06938 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5345479-bfa5-3ca6-ad6f-3b8abae23422 | -20.89935 | -50.50641 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2cadb2ec-8e3d-3f73-9d62-f7cbb12b5fd3 | -15.36259 | -52.75281 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 031beba7-efa0-3563-8276-a3169b0883b5 | -15.36568 | -52.79243 | 2026-08-20 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9cba84-1524-3274-94f6-2c0b19b8b85d | -18.04241 | -44.61646 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e2a54dfa-f11b-3379-9658-5fc297720474 | -17.94104 | -44.41269 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0235ca1c-b8a0-39e4-9267-0732020378bc | -14.31937 | -51.94661 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24476e35-6f54-38a7-af45-fa22f49aec59 | -13.94158 | -53.86774 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4511242f-a21a-30ef-939d-d0a9c3fd7add | -13.44142 | -57.07593 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 066c6cda-e9b7-3358-9f96-e82df15935fe | -14.20349 | -52.88469 | 2026-08-20 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fce30f0-ab0e-382c-89e4-bd9d68f87b63 | -16.07205 | -54.96737 | 2026-08-20 05:08:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d746e641-795f-36a4-942a-7cbe52af5805 | -14.31507 | -51.91375 | 2026-08-20 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f41b05cb-050d-3c52-8241-efec28f71239 | -14.08828 | -58.81921 | 2026-08-20 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07bc230-ba99-35de-94e4-f18b031808e6 | -15.72342 | -56.17795 | 2026-08-20 05:08:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6358279-ec4c-3ca1-a543-9cf5af3bc5b6 | -15.90591 | -55.55219 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 228b43ef-3e5d-3c76-9ac3-811d223aa64c | -13.44197 | -57.07239 | 2026-08-20 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 559fe629-3241-3438-82b6-c4927d5e83b5 | -20.26578 | -46.74617 | 2026-08-20 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991f73dc-dd9b-37cf-98d9-b14a1ad62acc | -15.77071 | -55.56413 | 2026-08-20 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012c4493-4037-3c34-8aa9-f11b49cba2fd | -17.94157 | -44.40638 | 2026-08-20 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 73367a2f-3ca3-3db3-b8f6-9f741c199ece | -14.67 | -55.62791 | 2026-08-20 05:08:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1283498f-c194-31b4-8f9f-7428ae963c3c | -18.84513 | -47.14321 | 2026-08-20 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 592c70a3-eafe-3eb7-9d0e-41e375f30158 | -20.52825 | -47.53955 | 2026-08-20 05:08:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42d7f3f8-ff33-3d2c-862f-260a34ddfdc4 | -13.94528 | -53.86835 | 2026-08-20 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8335b4a8-6033-3a5c-bd4f-c7a666a35d36 | -17.3372 | -43.6139 | 2026-08-20 05:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 373d5dd3-758b-3779-84d9-7e5af74ea5c9 | -9.4256 | -60.4353 | 2026-08-20 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| d1ec243b-3d2c-33a1-9f51-a9f4082f4d83 | -11.8379 | -58.8248 | 2026-08-20 05:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 74d289da-b3a0-36ee-af00-712d17ff7db2 | -11.8377 | -58.8445 | 2026-08-20 05:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 7e493f11-0784-3f9f-bf98-5cc72348dac5 | -8.6727 | -54.6492 | 2026-08-20 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c2e5a390-6aca-3746-a39f-94076a6bf167 | -11.2189 | -55.0585 | 2026-08-20 05:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b0f910fa-bb1e-342c-85a7-4ee7a8f3494d | -9.4257 | -60.416 | 2026-08-20 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 633c63db-b794-38a5-845b-b27d0ef893a9 | -17.3365 | -43.6383 | 2026-08-20 05:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |


[Clique aqui para ver as próximas entradas](README57.md)
