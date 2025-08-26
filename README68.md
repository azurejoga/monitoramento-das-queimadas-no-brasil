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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7467afa-f6ea-3af6-b801-dd02f8176358 | -14.64075 | -49.07778 | 2025-08-26 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 15593ecc-a766-3a8b-9a15-faf6b5123a35 | -14.36149 | -51.91988 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32abfaf1-5142-3f64-ab50-1d3f65cfc70e | -9.23665 | -60.92017 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f715883-f48d-3d3b-bb9c-7588809eb21d | -13.6407 | -45.70307 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1795c6f2-4e9d-34ff-b5d8-c0e161f5b731 | -10.87178 | -55.79497 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe86b638-dc7c-315a-8043-4175f69be046 | -9.26347 | -56.90217 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 024a0e6f-f605-39ad-ae97-c55f38cba316 | -8.60157 | -62.59153 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00fd5da5-de5f-39c5-aad3-93b232caecd7 | -8.56819 | -62.62406 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50658b52-7239-3336-b670-385f93d392aa | -7.38055 | -64.36327 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6a98f26-0bd5-3a76-8111-2ecc729e1846 | -8.56221 | -62.62297 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bac001f3-8d39-36d2-8dd2-7662aa58d88d | -11.57132 | -52.12203 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 93c0355e-2abd-3da1-94f5-357df7aee1a1 | -8.10981 | -62.87889 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 296667c8-6cbd-396f-962f-6ef2c60b2536 | -10.89701 | -55.78057 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed24173-2823-364f-8c94-46e6c1c4f3d3 | -12.4259 | -45.96616 | 2025-08-26 04:46:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4f17e51-86a6-39b9-87f8-38bfd00b415b | -12.33443 | -64.231 | 2025-08-26 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20354265-3402-3b31-8ae1-c09492a376f8 | -8.55831 | -55.26004 | 2025-08-26 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4e605aa-c1d1-35ca-b42e-e1cbc9b4328a | -15.083 | -48.55335 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| be2d6918-5905-35b6-82d5-1c66914b2434 | -8.57434 | -62.6368 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8289c458-a7d4-3b81-bf67-f4adad9d045b | -14.27759 | -49.13824 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa4102d9-c41e-3ed1-a52d-417ee0147563 | -11.54744 | -51.88411 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf1e7195-f293-3d91-9d10-cb546487d227 | -10.87067 | -47.34583 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b74515a7-2ed6-3647-8622-db00c64c0efe | -9.79543 | -64.2543 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6086cb6-65d3-3033-92c2-07e098e6090f | -11.62734 | -46.21431 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 743c5592-bdec-3200-9e01-ebc6bf4cca2c | -9.00107 | -65.40691 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7538cf8e-aa3a-39cf-9040-1d475184d170 | -9.26691 | -56.90643 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b5e5a2-baea-31eb-8a26-9922853d1a84 | -9.07111 | -65.72327 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c37fe2b-86a4-364e-8a7d-3fe5a02c724b | -13.44125 | -47.00017 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4bcfb16-9f42-34f8-b114-bb5e07e4b3ce | -12.95573 | -46.32722 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93b928a9-769b-37d6-b765-0732689a9212 | -13.45603 | -46.99276 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5411141d-36f5-38fe-8dec-aa64106b5b24 | -9.23787 | -60.91365 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e5cf45f2-92e9-3d3c-95c5-0367971b0d53 | -15.02192 | -48.50213 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a491d08-2934-3b76-ae59-bd3d136649fb | -13.43572 | -47.01736 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eeb8fc6c-3faf-308c-a539-85b3defc0719 | -8.10338 | -62.88067 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03dedd8e-18f5-3943-b814-70c8839f2e88 | -13.40193 | -51.7681 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8773902-74e9-37a9-93ef-3bf4fd31e139 | -12.78238 | -48.13718 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1aab2b47-22e1-310f-966d-f5d9f61aaae4 | -13.60163 | -48.19752 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdd23640-9be5-34dd-8121-8d2403d328e7 | -11.15603 | -44.75301 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7514ef09-269f-3c50-b317-f4565c6c6b47 | -8.86116 | -62.43449 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7371d80-4f84-3ebd-9ef3-1ef2ea3edc47 | -9.16985 | -59.52774 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14848b92-2cd2-3152-9463-498c3320471a | -9.1745 | -59.53818 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 246f1416-eed1-3ba8-89b2-5dc56b80caa8 | -15.0226 | -48.17109 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c3bdd85-372e-34fd-8fdf-8be5277fa32b | -9.17154 | -59.5266 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 330f2bb1-c135-3ef2-a78f-ee806199da32 | -9.16906 | -59.45072 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6536dc24-e45c-3634-95f8-efdd90fbde39 | -8.59224 | -62.64024 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf0d7ef5-df13-33e7-bd2c-76692229dd2c | -12.7452 | -48.09188 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f60cfefa-5193-374b-9380-43fde2601d97 | -13.37189 | -51.78543 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f5b0324-8676-3c4c-bf04-94772f043ec7 | -9.63717 | -59.64299 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fd91f547-ea66-35f4-95b4-7b4eed2685e2 | -15.20818 | -53.79679 | 2025-08-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8de35d97-660b-3d3b-bd84-36743a26f2c1 | -12.76312 | -48.10531 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ba60d12-a212-37a7-a886-5882caae8eea | -11.30504 | -55.11036 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d08052b0-935f-3686-b00e-0b3316682295 | -10.39148 | -57.69295 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43530e3b-29e6-3710-b598-cdc82880b08a | -13.42172 | -46.92403 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074368b0-ef1b-3603-85ef-5106018962f6 | -13.42524 | -47.02346 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c58aa50e-3e08-3707-899c-3b1745f1c57f | -6.78761 | -59.67682 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1903dcb4-14b7-3ae5-a995-8ad7449ca9c4 | -13.43762 | -46.99547 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7e50bc6-5e25-3c1b-91c4-8cbd24a75141 | -8.36376 | -49.55904 | 2025-08-26 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e93134f-d523-362c-873d-06d82c37d552 | -8.11908 | -61.45861 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b477a1a-9773-3e9e-a8e4-ebfbe012b56b | -12.75778 | -48.144 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1744496-37db-361d-9775-360cfb60bef1 | -7.35546 | -59.66923 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c16e07c-9047-39f1-89e5-b1a0daa9c039 | -11.89192 | -55.134 | 2025-08-26 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c688935-9541-3aff-b09d-191a1f98b4be | -12.67704 | -47.85987 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9c9f97a-b2bc-3789-a1e2-c7a6358511f5 | -11.91046 | -47.59798 | 2025-08-26 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f09c513-6150-32d8-ba67-4ca5359165c0 | -9.16496 | -59.55447 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa530600-d224-3796-863a-3e89d9539c92 | -11.69784 | -60.17328 | 2025-08-26 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3de1f6ed-69c7-314b-8a48-054e455d05a9 | -14.72297 | -45.37545 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a3f9bbd-d654-39f2-b927-f6fe0b18291e | -6.76443 | -59.6717 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2874396a-a282-3fec-9f90-c6dce3388763 | -9.17273 | -59.53927 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a367b895-05f3-34a9-b1af-759f18c2bd48 | -11.53047 | -52.12263 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 76afb39a-389d-3095-864c-57282994bb53 | -10.24632 | -59.11059 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0da680bd-da36-3a31-85a3-f437427476a6 | -9.16295 | -59.54719 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2840ef51-017a-3fe6-903b-42081095a702 | -11.61821 | -46.41168 | 2025-08-26 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa3086db-8c1d-3b6a-855e-2b88419b61be | -13.45466 | -46.87181 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c832ebcd-dd78-31e8-b55e-77b79996a7be | -9.09218 | -65.72861 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 584f86fa-cacb-3b6f-b0b3-c87f71e6f191 | -13.44177 | -46.99638 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446e1834-5246-3b95-bba1-34b10f83283b | -11.53863 | -51.91876 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaff7116-56a6-3101-9804-2c492c2d092b | -7.47859 | -61.3618 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ac6dd24-d4b4-3f28-af57-7f1879e9c31c | -8.60663 | -62.65029 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ac40a80-f3f1-31ac-8247-3837b199a3e1 | -14.30541 | -53.06756 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 393c30a1-8a2b-3988-951c-a3639efb24fe | -11.30368 | -55.11855 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25827bff-a417-3eba-8873-7c306f81442b | -8.10371 | -62.8777 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07d0e147-1f58-3279-a722-2a4aab31e032 | -14.25005 | -48.04558 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b5416e4-f0b2-3c59-9d1c-55aba6f33da1 | -9.4703 | -57.8245 | 2025-08-26 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 892863b5-e4d4-3f0d-9e98-0b36dca9f84a | -11.52451 | -50.45267 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca58d5e9-50a9-32c6-9945-04c6d5d16e3f | -9.17342 | -59.51587 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5423e4ae-2b26-3128-ba4f-1f2516a90cbc | -13.45401 | -47.0081 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c1edb3f-0079-338d-9330-8f10c32a0c40 | -16.31917 | -43.62374 | 2025-08-26 04:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4459ad62-bdd5-3479-9c53-b4d1c6cc6e88 | -8.85019 | -62.4502 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 53b92e56-2a61-3897-9517-c389c059b53e | -9.23074 | -60.92246 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed612d9-1211-3c76-ad7d-b1678c8713bb | -9.80909 | -64.28661 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0298ad62-5e14-3c95-9361-070e12c51ba2 | -9.40805 | -48.24991 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6033396-e72b-334e-9861-4df305768cef | -13.4482 | -46.98726 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dd4ffb3-61e3-3da4-8239-a383a997a8ab | -10.53749 | -46.79835 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3f36b8f9-d0cc-3787-b905-04521b5137db | -9.22693 | -60.92065 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 615a4c66-321b-3867-9b87-e76cd1564ded | -11.16202 | -44.76837 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8667d21b-62b9-3fe3-80d2-334a6ec9093f | -9.80796 | -64.29229 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1220df-1fcf-3c42-85fa-14046dd99177 | -11.63094 | -46.41354 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09e905c2-52c9-396c-8e0f-0d799311c568 | -15.02445 | -48.51258 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc91538-c1b1-3791-be88-6cb77ff7b56f | -9.05663 | -49.56161 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0cd700a-272b-3581-aa00-744b1ac33233 | -7.39407 | -64.35596 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04ce491c-2c4d-3470-9134-1beef1fe22a7 | -9.10656 | -46.06439 | 2025-08-26 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
