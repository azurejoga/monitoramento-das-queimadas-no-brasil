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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7b35cdb-7018-327c-a8eb-8f29b51dd79f | -15.71951 | -55.87672 | 2025-08-23 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94d5ca94-7c52-3037-9da9-78b5a336920e | -14.78946 | -45.49948 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c049aae0-4d1d-39ff-9c27-6be31b4e0a28 | -14.66618 | -54.86473 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e326fd60-8109-3036-b177-45fcd4e3dd56 | -15.56487 | -55.01017 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2519311d-a025-34bf-becc-85e0b3a958db | -9.5209 | -60.54877 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09a81df4-2f12-332c-8ea0-5c927f8b728c | -14.72767 | -55.42017 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20cd6690-a955-3c4b-837b-659b452c945d | -14.6737 | -56.59674 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f06d19-48f9-3c8c-ad03-93f522eedfc9 | -13.02985 | -56.82708 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfed59a6-1892-3365-a9a7-15633eeac071 | -15.2027 | -48.26385 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7987238-34f7-3a63-a390-df36bbec8919 | -14.80812 | -47.94622 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f1de3fc-20bb-3c1a-8d13-79a50bffe08a | -9.51089 | -60.55192 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e19090-914f-3e13-aa65-7bc9da7e9f34 | -13.0323 | -56.86333 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3d69749-26cd-3c0c-9e81-5ac09cbb7d17 | -14.37927 | -52.04262 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07e8e7f7-74c6-35ef-8395-b0d737d88fb8 | -14.37771 | -53.35818 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddc5ff6b-333c-300c-8b31-711793109377 | -13.00264 | -45.22329 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e45b3f27-b09f-38a0-a9bb-ba014c144281 | -12.99738 | -45.2226 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1095c089-f42d-3541-ba9e-4ec2205b1b64 | -13.14038 | -46.9152 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4169e925-78d1-38db-8da9-97ab39fbf1dc | -14.27956 | -58.52995 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32bf5ed4-9f46-37f6-a722-61b3d01ee444 | -14.67885 | -54.87047 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d2f14b-1b99-3b82-96f2-77a2f3267346 | -12.70957 | -48.10187 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 397efe9e-574d-3407-943b-0ff7dc5ac140 | -11.18087 | -55.04089 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c677a54-de4c-33b8-ba30-a5f79094294e | -13.0288 | -56.86273 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a21409d-c0ae-3e66-a875-db3be54ad693 | -9.95859 | -60.19292 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 222.7 |
| 66b43b4a-3c42-3e7e-8a22-1bf9cb3546c2 | -11.19045 | -55.024 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19446172-a187-368a-b6bc-58c3ed4ca42d | -14.62292 | -54.8141 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c031c03-3de3-341e-8dcd-4108ded0ca95 | -9.52594 | -60.5202 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 136f2c22-aad3-334f-9ad6-d7cb35e62de5 | -13.37137 | -54.40112 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d44735e6-b888-3a89-8a8f-b3ea1dd5c8aa | -12.48939 | -53.8205 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a85e59a-e5b1-384d-9140-fc87ae74feb2 | -11.31155 | -55.14029 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a38f18b-6b9b-3a66-9922-645d7efd5fb2 | -13.02962 | -56.87919 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82b89840-21cd-38f6-bc86-79904a7326b5 | -11.09368 | -58.94499 | 2025-08-23 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a765d3d-aa0a-3a22-8522-3500be400322 | -15.91351 | -52.2293 | 2025-08-23 04:53:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75b53a82-8dcb-372b-97f7-71605a6feb2b | -9.23661 | -60.47493 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d230a3f-e0e0-3e5c-9665-71126577902d | -14.80666 | -45.44341 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36bcf30b-7120-32d1-bd15-b35e7f60e15b | -13.4335 | -57.17701 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48915723-f58a-3220-b73c-c451b81bc6f5 | -14.30993 | -58.55447 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd57e383-835d-3b27-b407-1a9f9785c905 | -14.67167 | -54.87293 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad433710-4a92-33a1-bb05-82f3b5ff6771 | -11.62248 | -50.42507 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be984dd9-4894-3d62-b7db-78a4ea48bd8f | -16.35509 | -54.73851 | 2025-08-23 04:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a223ec45-2076-395f-966f-976cc47371e8 | -11.20209 | -55.03698 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0f9bd0-d20f-3b23-9cc2-606a2e8b4bd7 | -13.36365 | -54.4071 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2c4489e-deaf-37ec-bcb7-f4e54436a2af | -9.51306 | -60.51305 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cee60aee-0ffe-3c31-a837-12653cbc23bc | -14.28065 | -60.38398 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a92eaa4-972a-36f9-a97b-5bd84ff55997 | -14.73064 | -55.38022 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5398aa5-dff2-3384-8869-be95750acaa6 | -15.22633 | -53.85782 | 2025-08-23 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ca293048-6a1c-3646-9a25-e712e27ef3f8 | -14.28299 | -58.55426 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c88a5a79-16ef-37ad-9b2b-85a412bebbb9 | -14.91343 | -47.99889 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 922c665c-76d4-372d-85bc-b418e3731bae | -9.94182 | -60.1915 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73517219-480c-37e8-a58b-7029ea047e66 | -14.37402 | -52.05409 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf1aee88-262b-3d0c-83f8-49cbe449b5ec | -15.65767 | -52.68169 | 2025-08-23 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91ab591d-5b03-3733-9012-c65b3a946dfe | -14.6487 | -54.88759 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c3d1ef5-653b-3896-ad31-91ba91390e66 | -15.58784 | -54.29263 | 2025-08-23 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77babbdf-6992-3a31-b780-97a059963d6b | -14.73581 | -56.02497 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fcbc1b1-f712-31bd-966e-b79c807043c2 | -14.7364 | -56.02131 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceb5d27a-3290-37c3-b9e8-60b4d5457c25 | -15.22967 | -53.85835 | 2025-08-23 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ae90ab49-7d22-3a9a-9489-eac93707ed5e | -13.41507 | -46.27582 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b74292ad-a6b6-30ea-bf37-2b1b6b8fb560 | -12.17698 | -47.21077 | 2025-08-23 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa06accf-0e28-31a7-ba54-eb6172df7b6b | -14.96246 | -48.66914 | 2025-08-23 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2bfbc5b-b6b5-366c-9d44-afff63e76400 | -9.95956 | -60.19475 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 2a3369f9-e62a-3e24-9b82-1cfc125aba61 | -15.54721 | -55.01454 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c9ec6d94-9056-350a-85e3-10a77741a3b1 | -12.54346 | -45.61411 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adefee4c-7740-3fad-aa9d-7e6863a50927 | -13.13219 | -46.90435 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d20a5b87-8706-3720-b40c-eb295bddbe01 | -14.86149 | -57.52237 | 2025-08-23 04:53:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68a5d690-c0b9-3cd2-88a1-f95b40d443a9 | -8.68954 | -62.86084 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d10068e-a53c-31d0-b017-0630bbfda2ac | -10.62954 | -52.34094 | 2025-08-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06c15df1-6d3c-3776-baf3-3901756c40a3 | -9.51632 | -60.54796 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbdb78ac-32ce-344f-9e61-60cc6f80efc7 | -11.19379 | -55.02454 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43b33718-4f86-311b-ba96-904726cec430 | -14.4291 | -53.33644 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf4f40e-5241-3d15-9006-159bb880e454 | -12.18152 | -47.21141 | 2025-08-23 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b373d14f-4b4b-353b-9652-9f140c9787a2 | -14.61962 | -54.81355 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c48850a-6a20-3421-b569-c337896f1010 | -15.06117 | -56.39606 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db616de1-132d-3af8-8fc0-a177d4a7baec | -11.18433 | -55.01934 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| badc2413-912d-3f1e-ac59-366db92725f5 | -15.00312 | -54.88425 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09748d51-6b7b-35d0-a046-79a1a70407a2 | -9.96177 | -60.17532 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6d4b03eb-6365-3253-8a28-03c323d6551b | -16.41664 | -49.14643 | 2025-08-23 04:53:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 131c08d8-775e-3c50-be85-47ec7447016a | -15.07293 | -48.50993 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d1cf46d1-40d4-3314-95a3-517b1ca8df70 | -13.03379 | -56.8758 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c290bb86-4c30-3089-9285-b3bf096ecdd0 | -13.02157 | -56.83378 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fe38923-c2af-3f0b-a27f-5d18d940403b | -15.02189 | -54.87276 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e953e8f7-ae40-30f0-b134-dc3900875fa6 | -13.38116 | -46.21302 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 883d85ed-44dd-3aa4-a5f8-223c09ea2945 | -13.39079 | -47.51283 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74a89def-74db-31c1-a6ad-dc65077409d8 | -13.37701 | -47.51234 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e7f51b2-f304-3f5a-9e40-03227c7ed520 | -12.49325 | -53.8175 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eea19527-4aa8-3a50-adbe-fa49dbda6c85 | -13.50943 | -47.0526 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f71e2f6d-06dc-3b5f-9ab1-fd169539b6a6 | -13.36476 | -54.40004 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61269205-9e81-3016-b634-3e73bab68881 | -13.34877 | -54.39382 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb2cffa2-936c-39c8-bd45-f77429473ca7 | -11.18814 | -55.03837 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec7b267-db3f-3e02-9633-9206af85178e | -9.95131 | -60.18256 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 773f50dd-57ef-3366-a229-a830783c7e0e | -15.02022 | -54.88342 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfb1feb3-3dc8-332e-bc20-b2b8cbdf13d6 | -9.10078 | -61.43608 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dea76bed-b854-3272-aae0-85729987df83 | -9.10177 | -61.43062 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4275a9a0-311a-329e-b13b-9ffbde99667e | -14.78568 | -45.48553 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02bbc839-4003-3d85-a4f2-0f876ab6f18d | -14.7853 | -45.48886 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d563bf6c-f70e-3530-a6a8-7c4044558c40 | -12.54273 | -45.62007 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1921e8ac-7009-3969-b90f-470a80aa58e7 | -8.88552 | -62.40428 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be72111d-0dc9-34e8-b271-62d015410dd4 | -13.45777 | -47.0272 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1af7cb8-8118-3266-a6b6-c98fef7b6eb0 | -8.69927 | -62.87762 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12512423-b10b-33c3-afd4-78f190ee40e1 | -14.38453 | -52.05571 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0463dde-0738-32a8-9fe5-4fe5da696fc6 | -11.97242 | -46.77645 | 2025-08-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a134d2d1-2cd1-3424-b95a-352829e81d8d | -15.01639 | -54.86455 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README52.md)
