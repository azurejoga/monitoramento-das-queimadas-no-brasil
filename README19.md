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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d283943-bb06-3422-b9b6-86494f07c227 | -9.29004 | -49.64139 | 2026-09-29 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbb43def-2330-3b20-8aec-56bd2f5f5bb4 | -10.5143 | -45.36714 | 2026-09-29 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b36b17ac-7636-3aed-a19f-e6dfa7237596 | -10.81813 | -48.74842 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb9dfbc3-31ed-3b77-958e-2f318adbae97 | -11.42701 | -43.47053 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 5be32a31-d843-3b3a-86d6-89e26dc702d1 | -15.18165 | -46.17384 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84933dd8-35f4-3518-aece-76037e2968d5 | -11.38126 | -43.39025 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cce8325-6182-3011-ba13-204c3efae378 | -12.55884 | -47.16186 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 836de8bf-2e20-3131-9d2e-c3db3263e001 | -11.33663 | -54.11678 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c148c4c0-afa1-3901-b45d-f38cd9f09d27 | -12.02993 | -50.96442 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c0da0ba4-1d68-3ae3-a00b-1267edc37d3a | -8.85692 | -49.88373 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89e06fad-5e2e-35d4-8572-c788ad803baf | -11.14729 | -50.07458 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7bb90a9-065c-300f-a53c-5cbce0942714 | -9.52682 | -46.36088 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e67686e0-d528-3c0a-9cd2-611978f6f28a | -11.71093 | -44.53598 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac1b06f-bb88-3656-b9a4-0fb2f8063d69 | -12.05836 | -50.21282 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97c83a62-dbb2-3d7a-b040-2629d79e7dc5 | -15.67193 | -41.03493 | 2026-09-29 04:17:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83df2a93-a462-3184-9b46-d87e918964f9 | -11.72039 | -43.4617 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d35304c-16f8-3725-8a8a-25a04550689f | -11.18957 | -50.05418 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f8db5cf-708d-31d1-a2d3-e3c6a00dfd29 | -15.16904 | -41.80997 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e7027eb-3a16-31c1-9572-eb35cb7d21b0 | -10.82003 | -48.74706 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7117670-15c4-37b0-9f7b-8942ee7fb603 | -11.43029 | -43.44913 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79243622-c8d3-3244-a47c-ba4f80349a92 | -11.86755 | -47.0844 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e6a0bf8b-459d-3c5a-9230-2175f71ec3cf | -9.85763 | -44.94024 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97bd33c2-20de-33ba-89a1-13c51750e8a7 | -12.17854 | -50.69128 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a2ff656-6796-3be2-bbc0-9f2069c27705 | -13.61188 | -44.40665 | 2026-09-29 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f06a1826-ab6d-3a4d-a0aa-5277108fe7da | -11.63226 | -43.50598 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f1ea45-a7ef-3ba4-994d-5bb9faceca66 | -12.69787 | -47.26171 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44bc0fbc-5479-39bd-9eb7-ec40da7ecd35 | -12.04169 | -50.94888 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef4526a9-2781-331d-a793-79850520bb4e | -12.01069 | -50.99646 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 246bdede-cba4-32d0-82fb-334f4d9a37ed | -14.99086 | -47.87215 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1b82ff6-1518-35e9-80a0-8220ce1e96d8 | -11.42308 | -43.45165 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4885a4c-c0a7-3915-a468-ff29dd8aacbf | -16.3546 | -42.58776 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c35984d6-13c3-3827-87ca-f09bd0d89f66 | -11.42641 | -43.45217 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f823f06a-a81a-3ccd-898f-e7b709a5e10b | -11.99431 | -50.96234 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 743834fc-f37e-37fd-aed0-8054592d92d1 | -12.73591 | -47.27904 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4426cefc-cc6d-3b81-b1fa-e62f2cc5be25 | -10.20095 | -49.9828 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97eb687b-8d74-3f9b-ae01-2e2de33364a3 | -11.40473 | -43.43782 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e96fe3f-590a-38cd-9479-6afadf42ca95 | -11.40861 | -43.43477 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e88ea7d7-1981-333a-a9d6-20061e34ab27 | -12.75728 | -50.66924 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59669e13-c1bb-3808-be20-74e5bacbcd5d | -13.37549 | -44.01865 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52097d08-8d78-363b-804d-8093e118c510 | -12.56297 | -47.15854 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4efa0734-7566-3dad-be09-4fe667fb3601 | -11.44028 | -43.4507 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 48c419c4-f583-35d0-ba98-85fab0eeb8de | -15.13164 | -43.62689 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 306ae55c-b5ed-3108-8bc7-82a18e470c96 | -12.74851 | -47.28952 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99250a53-d4ff-3cc2-9630-4d8037c4f112 | -13.11396 | -47.4035 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6be238a8-d96d-3fb2-9068-c304649186bf | -11.9887 | -50.9436 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ad33744-4322-3cc5-8ecf-20844c0bedf0 | -12.69722 | -47.26566 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 047361bd-9d6e-3331-8d65-c1a953c25517 | -9.79073 | -48.19561 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b716043-541c-3e2d-94b2-329038ad3e2f | -11.37718 | -54.05065 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47c12d99-faa2-3b51-bd1f-58d148a959a6 | -12.00992 | -51.00077 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd2e89b1-ef8a-3f89-8e71-565c3d8a550c | -10.20164 | -49.97888 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8843c88d-7723-3f93-a745-ed19946043d5 | -10.91167 | -43.85888 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75b759ec-795a-3250-bd5a-20dc8c268612 | -13.71738 | -48.83164 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4be037-3840-3618-bd0d-8523d07ba34f | -11.99306 | -50.94439 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb570d46-8335-397e-87dd-90cece77593a | -12.72957 | -47.27405 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b9f9c37-9cf9-3250-9fa8-21744ff02cc7 | -12.0625 | -50.21357 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f729f815-2163-31a8-a2fb-36fa3f14157d | -13.1917 | -48.54063 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6528c3ee-bc11-3140-88be-6a0f68d27d4f | -11.38738 | -43.39487 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 685605f8-7d7e-320b-9291-6ef031f8e94f | -11.40419 | -43.44139 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6483cb98-9fa0-3150-86f8-54a982a91589 | -10.80529 | -48.7304 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66966ed6-ede2-3d7b-add7-0f1fc98737fc | -12.01738 | -50.98432 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f622063-af3a-3066-9b2f-b993738e199f | -11.35606 | -43.35679 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee6e4998-af92-3627-84b6-9b9cf159e619 | -10.59477 | -46.2131 | 2026-09-29 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25b18afd-fb1c-34ef-84e5-b486142eaa60 | -11.42084 | -43.44399 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45ce97a0-8c89-390b-ac6d-0f75dcf9ba46 | -11.3623 | -54.0404 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756b76b2-b37d-30cb-85f6-5585ae7ce9b3 | -13.11263 | -47.41161 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f1b71cc-7422-3cd9-a26d-b32c6576e6aa | -11.96811 | -50.9281 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ea7efae-4de2-3549-a890-f5ba6dc44ba2 | -11.40194 | -43.43373 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c7bf92-6035-3df8-ac15-a76d231174ad | -11.99663 | -50.94947 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5843fc82-d3db-3cae-bfa5-3d37d99583b2 | -13.2667 | -43.55089 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb7a85d1-0b4d-3a43-985b-004d1207efed | -12.0479 | -46.50497 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95ab52c5-25fb-3bc1-be2a-0e42547b9757 | -12.02122 | -50.96282 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| baca8faf-7cb8-3aa1-b842-da6197aae4e1 | -11.38102 | -54.04022 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1a33f74-6f55-3b62-a093-7635ca964326 | -11.26114 | -43.53151 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3338997a-6f1a-3623-ac3d-27641543d4db | -13.19501 | -48.56566 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a47e693c-d2b6-36f7-8afc-2bfe835587a5 | -11.47612 | -49.73369 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6f80011-caf9-3f63-8f2c-9a14f5cf936b | -11.19672 | -44.80081 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 075a8372-4770-3478-bf40-9a70673423b8 | -12.74503 | -47.28893 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c88da7b1-bc6c-3f43-bbbd-08b43423e631 | -13.53722 | -41.41161 | 2026-09-29 04:17:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d51fe91-5e8c-316d-b300-50272d11f82d | -9.14395 | -49.9821 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52fab9b6-48d6-3862-a1b1-952dd9f0651b | -11.42254 | -43.45522 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 474981db-397b-3b6e-9b0b-a6ef71ca5096 | -11.4381 | -43.46497 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14273ee4-46bf-3cac-9e8c-3fbc4c6f6c85 | -14.49543 | -43.82418 | 2026-09-29 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 179dbb90-8366-312b-b1fa-ea45dd576ec2 | -14.524 | -48.29239 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6b0bbf2-e510-3f81-a3c6-96ab54bf6227 | -11.388 | -43.41326 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c24533d9-3c9a-3cb4-80fc-93601b5d7e03 | -14.53116 | -48.29364 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fc83f3f-794c-30aa-ba3a-882730ed14af | -20.38305 | -46.37494 | 2026-09-29 04:17:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 561d7f84-8977-37a3-8983-cb2aa28d9dc7 | -21.22972 | -44.33948 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c4cf0fb-3bee-305e-bd38-cc0cc9950e27 | -20.0139 | -48.31179 | 2026-09-29 04:17:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb7b2a75-83f7-3681-9f9f-253fc310e688 | -11.67682 | -44.53768 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbd1449-2695-338c-872b-fd6edf38ee21 | -15.46729 | -46.13368 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86e105fc-f912-38e5-aef7-1160db3d997d | -15.24594 | -43.27607 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 552bc91c-69b3-3c71-952e-4b9bd69f1036 | -11.98715 | -50.95216 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7889d60b-3eed-3607-b7b1-992fb81e54f7 | -11.62115 | -44.15219 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfc1d34d-db9d-37cf-92b7-286ae5a54d1a | -9.79143 | -44.8208 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 662819ab-f595-33e0-8e56-af598fb92f78 | -11.35013 | -54.04554 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9202038d-8739-30bb-8535-9154dd939156 | -12.69154 | -47.25659 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 54713138-1aac-3c60-af5b-508160d8298d | -11.3731 | -54.04251 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe362563-1e3d-3e3f-a434-c228a2740c04 | -15.45676 | -46.13564 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad6381e5-0d6f-39dc-80d2-490794612b78 | -10.82045 | -48.72191 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 625a6a55-5abf-39d9-9e2f-bdb5602ae3d5 | -10.43681 | -49.37676 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
