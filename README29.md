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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e0c821-6f62-3c22-8596-afd559fad1ff | -16.50095 | -46.59546 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca287279-6f27-36cf-9bf8-9a1db12cede4 | -17.09246 | -56.85615 | 2026-09-02 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f18f1e4a-048e-3acb-ab9f-c52aa3a6945a | -16.14079 | -46.64016 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70f0c993-e3c2-3d66-95e0-fba7181cf2ed | -16.18233 | -46.65774 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53b1d860-e133-3755-b637-58701e6cc755 | -16.14631 | -46.6484 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67201cd8-1d19-3907-b72f-ac4fca74aee1 | -16.50317 | -46.60318 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdbab898-5942-3f40-b3bd-3628778d953e | -16.73742 | -43.43047 | 2026-09-02 04:23:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45fdb3f7-0c9f-3b20-8caa-568206dc154b | -16.18748 | -47.49576 | 2026-09-02 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23e0ace4-2217-317a-9c17-f0e7e75b0053 | -15.65456 | -48.70967 | 2026-09-02 04:23:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b2b38d3-5eb7-36f3-822a-459a804612fe | -16.48619 | -46.60432 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca56def5-d3a0-3404-bc0b-9b348d985417 | -17.08718 | -56.85498 | 2026-09-02 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2dd8f50b-e809-32bd-b50d-76b8c57094e5 | -16.81366 | -43.91323 | 2026-09-02 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e2e96cf-f21c-3287-bcb1-f26b2de10e59 | -15.6629 | -47.26469 | 2026-09-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2d988db-7eb5-34ef-96c2-e80a331125ef | -17.53313 | -44.21398 | 2026-09-02 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e5912e1-443b-32a5-a6f0-48f38cb94603 | -16.1568 | -46.64646 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a22f16dc-2e9b-3b90-8e78-d1290d545756 | -16.15018 | -46.64537 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02e15234-b146-3e9e-b215-d2deb40a2242 | -16.15349 | -46.64591 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71c6bf65-ef90-3419-a080-349ad17be6b5 | -16.45048 | -42.41842 | 2026-09-02 04:23:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cbe6825-4bc9-340f-90d7-b1b2b7f7325e | -17.792 | -39.70895 | 2026-09-02 04:23:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ae173592-0d80-3fd0-b632-b2c80dad8a14 | -15.66346 | -47.26112 | 2026-09-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fd029f3-9103-3a1b-ae24-9ec6d8ed08a2 | -17.09316 | -56.85273 | 2026-09-02 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6103be3a-51b4-3742-97de-3d123a498b8e | -16.45492 | -42.41528 | 2026-09-02 04:23:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85c225ff-59fb-371d-b422-7c0661808bf0 | -16.15735 | -46.64288 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6c2d62c-c930-30e8-8440-694804663ee7 | -16.45035 | -42.41973 | 2026-09-02 04:23:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 357693b6-2ade-3e99-9a8d-9054c8b25459 | -17.08647 | -56.85841 | 2026-09-02 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7aa20c10-e4ff-3395-a615-4fdb5bf034da | -16.45441 | -42.41886 | 2026-09-02 04:23:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fc9726e-80e3-3b01-8ffa-984a3d2651b9 | -16.73569 | -43.42809 | 2026-09-02 04:23:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e362f6a-eb49-3f0c-8653-845a0fb25f5a | -15.6029 | -46.58094 | 2026-09-02 04:23:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a0f02fb-431f-3177-80a3-e4ed290b4038 | -17.67724 | -40.13894 | 2026-09-02 04:23:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 9ac3aaaa-07b3-392d-8c93-cc21207bf012 | -16.73425 | -47.06565 | 2026-09-02 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ac1895b-1085-3f4a-aac6-1a45c97291a2 | -16.73095 | -47.0651 | 2026-09-02 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7a40619-f7bd-3eec-b069-408135e9d806 | -14.4063 | -54.12889 | 2026-09-02 04:23:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a2f9b1-5d5d-3c12-8f4a-3002f746cc33 | -16.74477 | -47.04164 | 2026-09-02 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07d386f9-4fb0-30b1-a1f7-6ffff0b6bd8e | -16.14686 | -46.64482 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b351b3c6-2664-37ab-b87e-525fc1c549f5 | -16.49725 | -46.59876 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3269b767-4cbd-3df1-b895-8d693ab551b2 | -15.60345 | -46.57737 | 2026-09-02 04:23:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192c489f-a8f2-3214-a9de-59eb0a5ae271 | -16.50372 | -46.59959 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12977bf3-7226-31d5-86bd-66b393c35af8 | -16.99925 | -39.49771 | 2026-09-02 04:23:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 07e3d921-a6b1-3037-b177-eca4a8f07fa7 | -16.48288 | -46.60376 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 908fac7f-0fb6-3b77-b214-9d964718e506 | -16.48564 | -46.60792 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f0e670-e701-3384-bd1b-87781a912213 | -16.14466 | -46.63712 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 933aa63d-3bfa-3dff-948a-c6f22c68d384 | -13.55853 | -59.74498 | 2026-09-02 04:23:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1547e42c-8631-38c4-b3ac-ed7758f4b719 | -15.50336 | -55.14362 | 2026-09-02 04:23:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4725a822-8004-318a-bdaf-f14cbd51c2fa | -15.7398 | -48.29454 | 2026-09-02 04:23:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec564727-9740-3653-9892-3305fbc85079 | -16.13748 | -46.63961 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71f816c7-41df-35e1-bc5c-c970273d4aba | -16.14853 | -46.65608 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2d4757-c26c-3abe-add6-3bec9c7e8699 | -16.14134 | -46.63657 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17fab71c-1263-3051-beee-7c632c0247a6 | -16.15404 | -46.64233 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26c6b3fc-df2c-349c-a289-5caff9c9b11d | -16.18233 | -46.6357 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a7d1d05-e245-3b78-9f75-957d686050fc | -16.43618 | -42.40604 | 2026-09-02 04:23:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fd7e03e-5829-36ff-af07-5d992a6d7155 | -18.84734 | -41.97791 | 2026-09-02 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bdde381b-0ee6-3597-b675-c9a090171c98 | -19.20693 | -43.18423 | 2026-09-02 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7baefaaa-3458-31b6-9691-a321b8789849 | -16.49393 | -46.59821 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e03a4d6-4b7d-311d-b783-412b75826026 | -13.55722 | -59.75106 | 2026-09-02 04:23:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c086667-dff3-38f2-9605-a907e26f4e99 | -16.06094 | -47.06731 | 2026-09-02 04:23:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3b8563c-a0f8-309d-b0ea-e2c8166840e4 | -16.06038 | -47.07089 | 2026-09-02 04:23:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b69fc7a0-20e1-3d9e-86c2-963a9cd448e8 | -16.1441 | -46.6407 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e834eb2c-2079-37d0-a7e5-5e47dc1b758c | -14.40166 | -54.12794 | 2026-09-02 04:23:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 579f647f-9755-34fc-afe1-aaf4aa6aa395 | -16.16577 | -46.67699 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6915402b-acd7-30cf-a589-89d46944b13a | -15.65242 | -48.70153 | 2026-09-02 04:23:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e2a1a75-d550-340b-b21c-dac4719fc0a9 | -17.65837 | -40.25693 | 2026-09-02 04:23:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 98f0d953-9bac-3d8f-8d42-6f4305cf99fc | -18.5299 | -43.34985 | 2026-09-02 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b2dbf7bf-7128-31bc-87a5-72ac6e6f9d3b | -16.14742 | -46.64124 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b176d979-3c3d-3f3e-957c-e62827af308e | -16.15073 | -46.64179 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f6f2959-5657-32c2-a6a6-741a14358c65 | -17.65897 | -40.25195 | 2026-09-02 04:23:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 40fd71d8-73e5-3e37-b5e9-80463a85f9bc | -17.79261 | -39.70361 | 2026-09-02 04:23:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| de0ff1af-035a-314b-910d-c02dbb55fb2c | -17.09174 | -56.85957 | 2026-09-02 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 03c2ef34-0dc9-3aed-ab73-edf8c20ea45d | -15.83294 | -47.69406 | 2026-09-02 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57b2b0b-241b-3bdc-b00d-bed5ec769798 | -16.77464 | -40.46363 | 2026-09-02 04:23:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c347bab4-bf6e-369b-80d0-66933f028612 | -17.79738 | -39.70419 | 2026-09-02 04:23:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0c83778d-b8b1-3553-8d9b-070320c172e8 | -16.74202 | -47.0375 | 2026-09-02 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd217964-9d0b-316e-aeb8-9370495d207b | -16.50814 | -46.59293 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7396b122-f483-38df-ba1a-9df9f627ac01 | -15.66564 | -47.26881 | 2026-09-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49a44009-0083-3f6a-ad80-c3cec450d3e3 | -15.60014 | -46.57682 | 2026-09-02 04:23:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb6ab91-0fec-37f5-b4bf-d60c5734cd17 | -16.052 | -46.53319 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 049320f3-13f3-3fd6-88e9-5f770ea66c7c | -16.50427 | -46.59601 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dd509e3-ba63-3be7-9437-f4d4dee1d222 | -13.55461 | -59.74957 | 2026-09-02 04:23:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d943cf0c-1ee9-391c-a193-0ee017b8e4f6 | -16.17625 | -46.63101 | 2026-09-02 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ed2c43-b819-385b-92fa-1c54b6f2cd79 | -23.40791 | -46.42092 | 2026-09-02 04:25:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d1023b0-5fb1-351c-9d5f-51b48b34e7c3 | -21.89649 | -55.37288 | 2026-09-02 04:25:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a14a879-405c-351c-aad1-d33dbc21f5af | -3.2486 | -47.2438 | 2026-09-02 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1092366b-6a55-37b8-bdc8-c2203c4ce5ae | -3.2486 | -47.2438 | 2026-09-02 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 93ecdefd-dae4-3124-a9e9-ab5992492075 | -3.2486 | -47.2438 | 2026-09-02 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| dfbe044e-3a08-350f-80be-b62dff578ebd | -8.4856 | -54.7225 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 504e8782-04d6-392f-b0db-5742e789435d | -8.4669 | -54.7237 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 3159aef8-f762-36dc-972c-aca8283b8683 | -8.4858 | -54.7023 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| b08a8783-dd75-3ad2-bff0-f43545765a27 | -6.6948 | -58.7678 | 2026-09-02 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e6336be1-18f2-34fb-879e-d855fbfc74ac | -8.4483 | -54.725 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4f206b54-2bfd-30c6-96dd-214b6b26967a | -6.6764 | -58.7686 | 2026-09-02 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 06fdf151-502e-3f6b-972f-d8fb777c36d3 | -6.6949 | -58.7485 | 2026-09-02 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 6bb2d3b6-6133-33a5-92dd-feb85f1589dd | -8.4671 | -54.7035 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 163dc787-e8ab-30f4-9773-df28701855a0 | -8.4485 | -54.7048 | 2026-09-02 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cc47421c-3e3a-373c-83af-89017ef12a17 | 2.46579 | -51.11763 | 2026-09-02 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad061c04-7378-30fe-a58e-b1f118c56fe0 | 2.46702 | -51.11668 | 2026-09-02 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258165ca-ac32-39d8-9408-7abfc8d1d3dd | 2.51897 | -50.85171 | 2026-09-02 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6325d669-687a-3a76-8532-2f58d27317aa | 2.46357 | -51.11721 | 2026-09-02 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52ccf39-4e3d-316c-b9f7-8b5ab0217470 | -4.97015 | -55.85594 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19e60429-2783-3bb9-9a54-14cbc5e35b10 | -4.12001 | -51.03462 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb1faadf-74d5-3df7-9ab1-adb94eba389d | -3.62055 | -60.57248 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80080f18-dc53-36ad-9a9b-e732ad40b118 | -6.83628 | -41.68799 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README30.md)
