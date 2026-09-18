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
| 1dcd855d-9ea4-3c90-ba05-828342f2cfd4 | -10.65742 | -50.25134 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3959ceec-76d1-3464-9c0d-0331f5b37c91 | -11.67548 | -54.43891 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a4fc3870-7daf-345e-9d6f-6b5c71a024ce | -11.67214 | -54.45651 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d9572c6-4a5c-366b-9d90-6479588566c6 | -8.6008 | -44.51214 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a21b6303-c21a-38a3-8bd9-6f64a42373fb | -11.39866 | -47.63861 | 2026-09-18 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b35cdb4-52b4-3a87-aeed-6a23adda63da | -8.45217 | -45.83996 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aed1fe2f-2164-3b85-a596-240b3e4e4dfd | -9.75673 | -46.08891 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79568ebe-6c95-394a-9c34-b5670fe1f869 | -11.89267 | -43.8185 | 2026-09-18 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dcd8250-808c-34eb-a0da-bb157a4c07c3 | -10.62158 | -46.06323 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 119edfcf-cfb8-3ca5-8d26-dff8ddf48a19 | -12.39657 | -48.48028 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8f1ca5d-586b-318e-94c8-742c76785300 | -11.32513 | -43.35162 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 409a8c15-8b2c-3902-a177-f89e7dd939a9 | -13.42715 | -51.89836 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27d133ca-919f-313f-8c2f-bed306196d99 | -10.80513 | -50.19778 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d132dfe6-82ba-3ef6-aba0-a09d958323c1 | -9.48555 | -54.4822 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f39f778f-d6f1-3b3d-956c-d545a00c2e75 | -9.27439 | -48.24943 | 2026-09-18 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a82e94e-80cc-3a0b-b500-9e11865cca2c | -9.77767 | -45.03807 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96408dec-daff-342a-ac98-d6032581d662 | -7.50308 | -55.01319 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b650fd4-96c7-30a3-981c-db6af62d59c8 | -13.60511 | -48.29032 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5499bf0d-5393-3cd5-a16c-09bf86cbc946 | -10.64065 | -48.70646 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac11c64-b3de-32f2-810b-7931550fb8af | -8.94173 | -44.39499 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7eddc8a-f86f-333a-81c0-b1119c1677aa | -8.77341 | -45.89516 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aae1b00a-540c-30aa-aa0b-2c84a8f602ed | -9.94688 | -45.28373 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b310a5e0-6af7-3db2-9005-cb3a793b02ff | -12.33984 | -50.77224 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8292462d-ded3-346f-82e1-577346319fa6 | -9.94827 | -45.45183 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad35d0d5-ef83-3d08-9d87-44a5a0c56b8f | -11.13628 | -49.04435 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c6380f7-8800-3882-8269-dadff40e22a1 | -11.47461 | -45.71686 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 092951fd-089f-3dd6-ae18-b4470fd47706 | -8.44345 | -45.72029 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efa87733-0746-380d-934f-529e97b6895d | -12.96888 | -47.94702 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45cba3dc-120a-3594-ad13-a0e3f943124b | -9.91415 | -46.53507 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 115b9b7c-e342-3adf-9115-daf61ce501c4 | -9.24774 | -45.90674 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3a164d0-4346-3084-b901-2481f4c69d65 | -12.96772 | -47.95421 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0bae1e52-f224-3465-80bd-43b7d07425c7 | -12.05882 | -47.51092 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 764d90e5-08d6-3b50-a363-75a38187b311 | -12.39785 | -48.47253 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6915b48b-4d37-325b-be6f-a05a4ea9d3a2 | -9.92402 | -46.58035 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1717f272-43d3-3aef-afad-0a4f40f5663b | -12.39721 | -48.47639 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aab68222-2cb3-31ef-9f9a-b7b9f913280b | -11.89115 | -47.61834 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64fa0393-ecf4-3746-bbc4-72e42e9ec613 | -13.24755 | -46.90626 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1b02605-421c-3fe4-85ab-edacb315d673 | -11.87966 | -47.58261 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6afb1aec-031b-31fa-93dc-1e7c8ec8a4a9 | -10.66856 | -50.26575 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 72058bb4-e8da-3c0b-ae3a-2e081ea0a2ff | -8.50741 | -48.49844 | 2026-09-18 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4050c6fb-9027-3ce0-b94a-912038fb55c3 | -10.52311 | -46.72861 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8090c93-a311-3034-824b-b273fa9e6e15 | -9.90614 | -48.38264 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f426c029-d9ce-3ebc-aadd-e7307ae29c7e | -9.7091 | -48.14799 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d2acf8a-f1d3-3d5a-9265-1e38d2efa381 | -9.93522 | -46.53119 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62e12492-39b6-3445-8a10-824fe31a75c0 | -10.08459 | -45.58031 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41296301-aa03-3cbd-bfa6-8e449c706421 | -19.55444 | -47.63532 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 21ed00f7-f23c-3514-b8f1-b52f4ebda5a0 | -19.555 | -47.63167 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 28.9 |
| fe579e54-b33d-3c68-a6e1-41db4cd15bb0 | -19.18235 | -48.78696 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 52b9f289-1476-385a-b1d1-68e020982dc5 | -16.56228 | -43.99316 | 2026-09-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56b904a9-ed4a-31e4-9c54-f064459e50fe | -21.45925 | -48.6775 | 2026-09-18 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e97db7f7-0ecd-3eb2-a5b6-2be31335d71f | -19.17807 | -48.77101 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6829550c-f4b4-3e71-a10f-e01fad293265 | -18.84118 | -50.11589 | 2026-09-18 04:23:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 25ecc996-6085-3f6b-9e72-aa3cecc4322b | -19.17688 | -48.7784 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 419e3acb-3db7-35e6-b900-26fe88b7eb58 | -19.715 | -46.22229 | 2026-09-18 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd135035-d993-3ddc-9aa5-ebcf32b1e55c | -18.02332 | -50.94592 | 2026-09-18 04:23:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 69349e04-2266-33f4-8d2f-a0e575a6072e | -16.12168 | -51.92351 | 2026-09-18 04:23:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55199860-8ccc-31f0-982b-f4fa6b4c3bcb | -19.18413 | -48.77588 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9ce2f04c-d58d-3e97-8b3d-1165e99e2ead | -14.70316 | -52.44703 | 2026-09-18 04:23:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c20716-f062-39f3-aa98-c029513840ff | -19.19234 | -48.78871 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 080f1b3b-15db-302e-8198-75a206508a3c | -21.06813 | -48.46088 | 2026-09-18 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae076ac7-bea2-3955-9ebc-1c58f1bca329 | -19.18842 | -48.79183 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f9faa4e5-99f4-3544-9e0f-8ceda5e62b31 | -19.17629 | -48.78209 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8af688e-0b93-3eff-8bd5-7fafe8c377cb | -19.18568 | -48.78755 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 403af26e-5b0a-396d-929c-0f6183df6a79 | -19.11979 | -45.78799 | 2026-09-18 04:23:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a223ed64-250c-3902-9aa4-5927390bfa77 | -19.18509 | -48.79124 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 315c7312-d2ae-39a3-80cf-2f0229768682 | -17.77358 | -46.4817 | 2026-09-18 04:23:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e3cfea9-fe5c-329d-b4c2-321c7285b8c5 | -18.88637 | -46.84778 | 2026-09-18 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01f53f8f-914f-3773-9277-20e8f01d0394 | -19.18021 | -48.77898 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d43b731e-3b48-38d2-b365-9586258bfa6b | -19.17748 | -48.7747 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7bfe91c8-8cc5-31c9-96f0-eb48c04c331b | -19.18782 | -48.79552 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 62ba729b-4266-339f-bb9e-de34dfbc9ba7 | -18.02408 | -50.94156 | 2026-09-18 04:23:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| e2807eb4-b072-3cdb-afc6-060f2bc64c2f | -17.78895 | -53.13987 | 2026-09-18 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2252345-8e9a-34d8-902b-f086c105f673 | -21.46197 | -48.68179 | 2026-09-18 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a36172f2-64ac-339b-87d1-95b5f6df8797 | -15.66293 | -52.73044 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f5d0f63-ae30-383f-b8c6-13aeb54f3cad | -19.18864 | -48.76911 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1dbb3b8-1bea-35cf-b9f8-4a7fdc37909e | -16.54476 | -47.97698 | 2026-09-18 04:23:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a074dfa9-8f66-3d3e-be32-9e01cffcb54f | -19.94919 | -44.70678 | 2026-09-18 04:23:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d202ba35-5386-3263-a218-bddc84477bfd | -21.05317 | -48.46957 | 2026-09-18 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6732ce4a-002e-3591-932f-0a20aebb4b07 | -20.60441 | -52.84772 | 2026-09-18 04:23:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a938f7c0-d682-3d67-bfc1-5a5f5885abd2 | -16.61163 | -50.38197 | 2026-09-18 04:23:00 | NOAA-21 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057c184b-cc12-3a98-95e5-f0902095822c | -18.99021 | -46.94788 | 2026-09-18 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b7c4089-ca53-3b61-ba8d-f6634c32f891 | -19.18901 | -48.78813 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e9aa88ce-d34b-3528-a4fe-8cfc9447a919 | -19.11693 | -45.78348 | 2026-09-18 04:23:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ae63e5e-f4d3-3d4d-9d5b-940d19b15f3c | -15.6381 | -52.72539 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1018713f-7f8c-3d50-b317-b2f590ea0f77 | -15.56707 | -49.93918 | 2026-09-18 04:23:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d345f09-af21-3b23-bb00-40aba7d20259 | -19.28312 | -50.36824 | 2026-09-18 04:23:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2a22f24-2106-3e88-8d39-0b932e60debb | -15.34948 | -48.10912 | 2026-09-18 04:23:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1e49d50-589f-32b2-b087-10fcef189400 | -15.47144 | -52.87455 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81fc623d-a323-3ff2-93bb-11645170019a | -19.17902 | -48.78638 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2546f19-e0bf-32d5-b47a-1b5bd9dd1f75 | -20.96842 | -45.79373 | 2026-09-18 04:23:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acbedb78-8275-36fe-85f7-e16217fabcd0 | -20.7774 | -49.21561 | 2026-09-18 04:23:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 50405846-fc01-3874-97e6-fbe89de694e6 | -17.83606 | -44.84717 | 2026-09-18 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d51ad74-f95c-3ed8-b11a-7077d33ed323 | -18.77087 | -47.73294 | 2026-09-18 04:23:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c3f4ed3-24a6-3236-8326-a97532321c02 | -15.57541 | -54.23859 | 2026-09-18 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6256bbd-8f55-3e18-96b3-d67ac01a6418 | -15.56721 | -54.23172 | 2026-09-18 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef6a365-93d2-3ac1-ae9c-8ec842b40d3d | -17.23411 | -46.78923 | 2026-09-18 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df317ea2-9040-344b-bad3-4b14bed65996 | -15.63879 | -52.7216 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3f86291-41e5-3a84-940c-3ac40af3477d | -15.2584 | -49.11773 | 2026-09-18 04:23:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f7a0d0f-6e31-3859-8a44-028e42f85955 | -19.18805 | -48.77279 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dd8d34d-340b-37fc-9c0f-d02ee67cf165 | -19.19079 | -48.77707 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README52.md)
