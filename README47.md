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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c9094f-1cf0-3c0f-ab21-3ba2e742cf54 | -13.1563 | -54.36145 | 2026-10-10 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd63939d-21b3-35e2-a48a-ef989d340439 | -11.69151 | -47.28791 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5c633e6-9e42-34d8-83c0-ef29a3a0d121 | -11.02162 | -45.42359 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f525de04-65e2-356c-9cbe-172570939823 | -11.86685 | -43.58471 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 179bef1a-ffe1-3bf1-be47-99b50cd0b5a8 | -11.76744 | -43.52515 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2243e386-aa97-37cb-b855-7e6a4cd53dc5 | -11.97622 | -43.45066 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cfe45b4-3432-3647-bf0a-20c4c7190013 | -8.64513 | -54.53893 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b32dc3-07e7-350e-bc1e-aa4faf76fcbf | -10.73322 | -52.03377 | 2026-10-10 04:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aa70852c-7162-3459-96f2-5b5d30418726 | -11.02123 | -45.41957 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6e6a837-f807-3594-8195-1102f979fd13 | -17.46247 | -45.08589 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6308fbed-d682-36b9-8128-f861aaf65890 | -11.01487 | -41.91275 | 2026-10-10 04:10:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 832687ca-ad88-3855-9aae-7775f7f192a9 | -10.89666 | -44.79936 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 99dc5ea4-8e9b-352d-b107-a4847684aa9e | -11.95691 | -43.48726 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51979db3-524b-3d4c-9312-513109bdab99 | -11.37545 | -47.57066 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd08c551-b68c-3553-98ed-f1add787792a | -12.93169 | -47.43726 | 2026-10-10 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec4096b4-9602-3d8b-b4a2-7da854e4fec1 | -13.16619 | -43.28517 | 2026-10-10 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0209e884-7acd-3d01-9093-fad5bbf9a7ca | -12.02732 | -43.47389 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3854366-16b5-316a-9b2f-8fb2f8213ea1 | -13.52987 | -48.43306 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd145146-42e3-30e0-bc3f-036847e65a80 | -11.00568 | -45.40454 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deeb42b5-6335-35cd-b26f-3eb9f2da883c | -15.2698 | -42.38094 | 2026-10-10 04:10:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 38605091-4560-37b7-bf5b-b623b40e9bd9 | -12.04496 | -43.44798 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e450a211-bedd-3e3c-b0c4-64210e475fc6 | -11.21148 | -45.21637 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cfd6156-2d8f-30f6-87a5-5db911e1ca98 | -12.58514 | -44.14005 | 2026-10-10 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e148b76a-99d8-36d7-8124-6f9fb526b6b0 | -17.96175 | -42.49316 | 2026-10-10 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1bfcd979-ef5b-30a7-976c-be165123db38 | -11.71943 | -43.63305 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14efef9e-8c40-36bc-b8b0-c1a6d1f2d574 | -11.08626 | -44.10354 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e5abf4b-339d-3468-ae8e-42ac8275534e | -16.00877 | -43.5989 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19e3ca8c-9500-3b1c-8f3d-b3f0d1b15481 | -11.87923 | -47.35843 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44f9d1d2-6705-3b8a-a036-4e9ccd2fc83b | -13.15538 | -54.36599 | 2026-10-10 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7920fdd-de9b-3fd2-8d89-63f1daa8b556 | -11.08672 | -44.12214 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8122effe-e5f7-35d1-b4b5-e1e09c8fe188 | -13.25615 | -44.01003 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8558e0f0-9dc2-3b8f-9ddc-41ac7f82a688 | -16.56573 | -46.80053 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99cbcda0-3c43-38be-b53b-5d3dc0e18e68 | -14.38611 | -54.97752 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c37c14a-43fc-3bba-b1e8-fcd6fe591a3e | -11.60263 | -43.74767 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 36058a55-5735-3006-b492-ed9cca26e0ac | -8.49818 | -54.60775 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46e92713-8cff-3767-ab3a-885d142c505e | -11.74372 | -43.62978 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0ddb4db-770e-36c5-9c70-2704739b0084 | -12.0295 | -43.48151 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af221926-d53e-3630-b251-6aab5cb52694 | -14.01093 | -43.2571 | 2026-10-10 04:10:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20dc9cfc-aa64-3283-b1d0-4fd072803810 | -15.10541 | -43.63248 | 2026-10-10 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29f2ffb0-2554-3eb3-b583-fb385d2af702 | -9.91362 | -48.12596 | 2026-10-10 04:10:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 028fa924-c0ca-3f44-b0c1-29a2e715324f | -13.52587 | -48.43235 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05841199-bde4-3ce5-bcf7-967f48da1faf | -15.46548 | -44.309 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b61bdf15-7f9c-3002-b493-c21d61756f7f | -12.6946 | -43.07856 | 2026-10-10 04:10:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 626dd499-16c0-3960-ad1c-06c4a5dbb508 | -11.09065 | -44.11908 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5e31288-69c4-33f6-b632-c9475f28b171 | -10.89362 | -44.81821 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e57e45ef-f09b-342d-8514-05d92df0018a | -11.87347 | -43.58578 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43853198-8401-3b5c-9b93-562794c3801b | -16.7199 | -41.88343 | 2026-10-10 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5ae465f-0c78-38e2-b2f7-e5fb45b31d71 | -10.887 | -44.79384 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 432d156e-d250-3c52-8548-eade589f1478 | -11.77737 | -43.52676 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb69d0bf-15f1-3581-a047-37529ab69578 | -10.45751 | -47.84266 | 2026-10-10 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b794102-7b30-3e08-99ee-372e932e9cd1 | -11.98171 | -43.45885 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c629de1-7fe4-37b4-b835-26136c5235c7 | -11.67401 | -46.78351 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef435e3c-5d90-3f71-9937-2e701ba455a2 | -12.0191 | -43.44014 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2db87d7-9857-3c91-8ac3-1af38ff4164b | -11.88224 | -47.36398 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71167d8b-165a-368b-9c14-04bccf43f8a0 | -11.02568 | -44.05293 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00264b5f-11a0-34b7-9a24-85517625d1a1 | -15.98608 | -52.48866 | 2026-10-10 04:10:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d53c91-cfbf-32bc-ad18-f285b0411b26 | -10.89423 | -44.81444 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e04913e-1bbf-301c-a847-764c7362d5a8 | -11.66844 | -43.69725 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 245e2389-410b-3f85-85ad-5744d71be953 | -13.80676 | -42.66128 | 2026-10-10 04:10:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca652c3c-a49f-345a-929f-cab86c573e00 | -11.59656 | -43.74299 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d03a1d28-3e52-3bc4-abab-8722e7b265b6 | -15.37678 | -41.92005 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92f4d9b0-72cd-32df-bcfa-b18c09bc94ea | -14.46118 | -43.9659 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cd923ea-f477-3d2d-9d73-5e9b57415239 | -16.6064 | -46.75653 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec9190cd-d26b-36dc-8b68-1a3dfcd0433a | -12.0262 | -43.48095 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e43cf05-6398-3822-822c-06132468a3e1 | -11.46333 | -43.38176 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450c8526-381e-3595-8b27-394d379fc8cf | -17.22818 | -42.93063 | 2026-10-10 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e75225e-fb38-364c-8d1f-4ee80b63093c | -15.02816 | -46.26561 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a9e9e6-650c-3baa-ad94-28c85369e2e1 | -12.91046 | -46.96725 | 2026-10-10 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfa0e404-c058-3ae1-a54e-baf10c07cb14 | -13.2639 | -44.00406 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6856a3fe-cfaa-3355-9d3a-e6a02e03e1c5 | -15.58126 | -48.18867 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4cd7ce2-1470-31d0-9bc7-a6a09a486f6d | -11.0363 | -44.05097 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75d41e3e-027c-32cf-b59f-42054dcb0acf | -14.44755 | -48.12643 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ec8489e-5d19-393d-aa3a-babad177cae6 | -12.78107 | -44.88634 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a813b8f3-d66d-3c48-b21b-65ed0ab0548e | -13.25671 | -44.0065 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8740bc5e-5a50-3eec-830f-2a70a43db74b | -9.6301 | -48.87646 | 2026-10-10 04:10:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 19ff4960-4c6a-379e-9534-4e089227890b | -11.01812 | -44.06306 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffb27f7d-e057-3ca5-a371-810795ee5c05 | -11.6011 | -43.69287 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 813b4878-5e64-30a9-a990-dc1fb94fc580 | -9.99506 | -48.00063 | 2026-10-10 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ad4352f-7aae-32ee-a7a5-4de30561e406 | -13.51576 | -48.6084 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f9df9634-9559-322a-9e95-7b375fcbb038 | -9.51297 | -54.67554 | 2026-10-10 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28802b68-661b-390a-90fd-4dd745a323ed | -17.95776 | -42.49663 | 2026-10-10 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7f69796-e4bf-3dad-b0e0-c447ca97b19c | -10.89886 | -44.80749 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b94d26a-88de-3ea8-96d8-5d41ba4499fe | -14.45357 | -43.92823 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc18d359-10d1-345c-9f5a-dc123f6f7aec | -13.37477 | -43.90577 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96f18381-66f3-32d6-be40-0773aaf40c4b | -13.14805 | -46.33422 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c1b39dc-a531-365c-9d58-200dfb77cfda | -13.26002 | -44.00704 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05016c23-dd45-37c3-8344-d32bccf42249 | -11.04977 | -49.56218 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e8f59ca-bc1b-3620-88da-6ff5e3b912d5 | -12.04112 | -43.42935 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5a6a974-a311-3d53-a994-3ce9cc7a4c77 | -11.974 | -43.4648 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 162da6f3-3b8b-3c1c-b7bd-a188ab8ce41d | -10.74619 | -48.53849 | 2026-10-10 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8834180-dcbb-3e6c-81e1-cfc9689a9b04 | -11.09076 | -43.98977 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f8cda98-f145-37f5-86aa-a114b8d3c9f2 | -11.0972 | -47.63831 | 2026-10-10 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eeb0df5-8019-3fa4-8e89-237014d79acc | -11.12286 | -45.95089 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0b5824f-d305-356e-bd95-10d470f321bc | -12.3405 | -48.19292 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a26159a7-ffea-3b0e-a39b-e0d69e0bea43 | -16.23974 | -44.05795 | 2026-10-10 04:10:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 555cec0e-8db4-33dc-9e84-42e5de6ea0cd | -12.14562 | -44.70864 | 2026-10-10 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cf6e554-2401-356f-b43b-8ec1ebc0efbd | -13.3792 | -43.89924 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2f500e2-6fb9-3ca0-9541-2f59595c0d42 | -13.91332 | -48.91858 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831c1e75-0922-3251-914a-91ebc43f90e7 | -12.49737 | -51.2935 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f636ed3-1266-3219-86da-de2a17ce1448 | -9.09791 | -54.70126 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README48.md)
