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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8808e2d5-b3dc-3171-8556-08627ba9a858 | -6.30925 | -47.63095 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e847043e-758c-320c-8e94-3272ca464b12 | -5.26228 | -44.48595 | 2026-09-20 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0128edd0-e9a2-3eba-ba56-cf1df44a5675 | -5.38301 | -48.41578 | 2026-09-20 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c2d77ab-1c19-32ab-b7dd-8fdcbfbf5a25 | -2.79315 | -45.69207 | 2026-09-20 04:38:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f9e6a36-8023-303d-8f6c-ff9f937dfc40 | -4.76704 | -39.57962 | 2026-09-20 04:38:00 | NOAA-20 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad181e22-d49e-3e48-87fc-8f8c8c1fb87b | -6.32305 | -47.62957 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 00b76ec9-b901-32be-9783-56d529b7de57 | -6.98001 | -42.17393 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2b4b3f8-56c9-3192-98b8-c8e31f113352 | -2.81524 | -54.71997 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62740ab2-2122-3587-92bb-6ad2d72bedcb | 0.69501 | -59.55805 | 2026-09-20 04:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d5616f2-871a-3636-94c4-ab4730eaac3e | -7.02443 | -42.07932 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2c04a3f-bcec-34dc-9d5d-112fe74535cd | -4.89443 | -45.63019 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 366cd70f-3f1d-3da0-aff4-4becd2129f99 | -3.14362 | -57.89606 | 2026-09-20 04:38:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d000bc4e-8e8c-3cb6-81ec-f14b3776967a | -6.28157 | -47.59108 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92d8d0be-2d8c-338e-922d-83cfd2445c1d | -5.55242 | -45.54166 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b575286-f3d9-37b5-a9b0-ca8eac02b7bf | -5.39646 | -45.89225 | 2026-09-20 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31dbc27f-86f5-3857-ba92-dfa14875a747 | -6.1814 | -47.49315 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43b3e989-f138-3298-b910-e96c78288a32 | -5.46016 | -44.31747 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 004de2e7-cba4-3d25-adb4-dfb90cbed1c5 | -5.73452 | -52.23522 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3d15187-857f-3593-b3f9-c78e6022f8f6 | -4.84366 | -40.5294 | 2026-09-20 04:38:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4677c879-2467-3f8b-8df2-5fa1bc524cf3 | -5.43622 | -47.61013 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd4ab95e-de0f-387e-88f5-f247180d870d | -6.97338 | -42.17426 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9db0e384-aaa0-37b0-aab2-505be12d151b | -6.54531 | -44.13463 | 2026-09-20 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dbf9577-ff96-3a22-ac25-72acdcea8d44 | -6.59627 | -44.90676 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eb2559da-88e6-341b-b86e-1e4cf9fa8a58 | -2.88239 | -57.82453 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2fa9b11b-d09e-3f5f-8c49-25f4df775594 | -2.97851 | -54.77261 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c183816-115d-3fad-832e-3a5900a23536 | -1.31806 | -49.277 | 2026-09-20 04:38:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40c3bc5b-51d0-3bd9-b437-38784134402b | -2.88167 | -57.82872 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd306fe0-2ab6-39a8-b662-f16f4d91d8b5 | -5.20858 | -49.34245 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 046df929-8846-3393-9f29-f47d2180d4de | -3.49542 | -49.50847 | 2026-09-20 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e53af067-4c16-3882-ab6f-7c0af416e01b | -2.14179 | -46.85364 | 2026-09-20 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b27961a-49d6-3417-a359-750b9d894e76 | -3.6876 | -60.62275 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c466b60-823b-3d3a-a229-576168d34383 | -5.67276 | -45.30107 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3f1672a-6cdf-3bc1-9388-d400cd7e2349 | -5.8358 | -47.79006 | 2026-09-20 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e48d384d-6740-3ee7-ae17-6ff3fe7a2bc5 | -5.83911 | -47.79058 | 2026-09-20 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0f48d01-5082-37d3-acd4-625984af24bc | -4.48914 | -55.48644 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c516a4a2-9204-30ec-b0ba-4c1ab31af96a | -4.28173 | -48.58808 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c171e765-e567-37f4-8977-039353db726f | -3.8467 | -51.3385 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94f38aa6-66b1-3cba-9c47-80f94ff4aa15 | -6.96898 | -42.58118 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cbc7fc00-223c-36ef-9ce9-a9964ce74202 | -5.85942 | -49.78951 | 2026-09-20 04:38:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8332f537-846c-39a1-bc8a-c6a05e32fd28 | -6.2012 | -45.32152 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec70038e-781e-32b9-b3ad-539a80b7f118 | -6.20875 | -45.34315 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85850a99-11f6-374d-82ef-fe72c0a4deb1 | -6.92469 | -42.91139 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddd7916f-4d39-3191-86d0-09862e8bc650 | -6.60288 | -45.53315 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43b02bcf-1f23-36b0-84d8-e275422ca844 | -3.97964 | -48.93399 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2be3687d-1197-313a-bae5-806e8fb3af94 | -6.30795 | -41.75487 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93f39125-4a5f-335e-8c15-1a69042a271b | -5.58479 | -45.56224 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40aa23aa-3f79-3449-ae8d-c6f7637eb489 | -3.37409 | -50.44257 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c124efb8-9282-3714-ae94-a4c8d9fa8dda | -3.89306 | -49.06427 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0d3578e-1b30-37c9-8a48-b55bcdecbbd1 | -6.5616 | -42.55973 | 2026-09-20 04:38:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4c380bdc-5410-3d73-9f62-5ef1cebf8403 | -5.40187 | -42.9483 | 2026-09-20 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0516d089-37d4-304d-9089-2e1313792476 | -5.92244 | -46.00181 | 2026-09-20 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6dc519db-feab-306e-9812-d422aed3aba1 | -5.4597 | -44.3153 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfb2ed40-294a-324d-a944-ecfffc4a30e3 | -3.14434 | -57.89189 | 2026-09-20 04:38:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a93bd582-90b9-37e7-b6b1-4a9cc459589c | -4.22687 | -47.54575 | 2026-09-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7edb9196-b1be-37e8-81c3-98aad4196c69 | -6.41329 | -43.87928 | 2026-09-20 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13f38536-0bff-3a8a-b7c9-291cacd119aa | 1.26109 | -50.73782 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 504ccd7a-8be4-3a32-bdf1-9198ad259f51 | -5.41287 | -48.44191 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74f29185-18e6-3568-8a79-135e83986345 | -5.76905 | -47.28588 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805bac5e-2383-3646-a9d5-d3d7e877ad0b | -3.45499 | -50.61574 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdab51f2-885e-31bc-a004-cec434648183 | -2.14482 | -50.90167 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 557dac2f-4f71-3996-9a78-160ea4546ea7 | -3.89586 | -49.06842 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 193c0204-71d8-3cc8-b844-c231f8852412 | -3.56907 | -43.48247 | 2026-09-20 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8776df1d-7347-3ab3-94f8-ad95d611e55e | -3.56977 | -43.47792 | 2026-09-20 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c97438c7-0a90-31c8-a26b-0cf29691bfb5 | -6.17631 | -47.71965 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5952204-9963-3442-91d9-bddf6c3f0d06 | -5.83083 | -44.1312 | 2026-09-20 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6899cd42-f9bd-3dc8-90e2-e9c01cbad63c | -6.173 | -47.71913 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 084a41d5-c65a-3844-a547-a0b8b48dc939 | -5.23897 | -44.51697 | 2026-09-20 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e95fce2-1549-382e-86cd-81a2d79a2b6f | -7.09495 | -42.08183 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68347694-14e2-3364-8a76-7eaa7af5fa96 | -3.89296 | -49.08652 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cdc8c61-e64b-3b83-8f4e-b3173a55b3de | -5.45949 | -44.32177 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bd8bad0-3836-3396-9e81-f6fbde61e0c2 | -6.2824 | -41.77697 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8705c844-981e-30ae-9559-0dead74ad956 | -7.09227 | -42.08054 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64ddfe8c-e0ca-3597-bc3f-76ae6f8526c1 | -3.48158 | -59.5913 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f257b0db-3c3e-31ea-b9b8-10483d5f8c06 | -6.20756 | -45.35096 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e725a58f-a565-3d8f-99dc-904c276e4d4b | -1.52973 | -49.19921 | 2026-09-20 04:38:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cb22d87-07b7-35e7-b682-3c835ed509a8 | -5.79356 | -47.36808 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 148e55d2-debf-3c2c-9a3c-1e1dd6e7d18a | -5.86615 | -51.56442 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a65b82e-e0e3-3669-b455-80065f02c65c | -5.45581 | -44.32122 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0df7e73-ec9f-3696-bbf7-f2b49598519f | -3.73832 | -51.82229 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 56723099-bbad-3ae1-8fd2-7e58be86e840 | -2.64354 | -54.69026 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 49922466-d3c3-3d29-a174-236fdd379bad | -1.63693 | -55.15403 | 2026-09-20 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0ea19cc-9fa8-372f-8c2a-c9f03d202481 | -3.44548 | -50.60559 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb9afc37-5ec4-36b6-8690-7ee5af36d82a | -3.34484 | -42.77056 | 2026-09-20 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 949f463f-ff02-36d1-8b97-b7eb79ab586e | -6.96848 | -42.17765 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6dbeb1bc-ff83-3d7d-9b5c-dd954ed9881e | -3.84395 | -49.06009 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8659480-be19-3193-a6db-5d46ab30f784 | -2.61225 | -54.76274 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 56220568-8b01-3c15-953f-196591b34de2 | -3.45204 | -50.61094 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8a78ad7-0d52-33ad-ad51-c4b54b96caf0 | -5.45279 | -44.31639 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26eafb45-6274-36c6-97d6-e50794ed5af1 | -6.27826 | -47.59055 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5836f79a-2ed7-3368-a665-7c716e97e58f | -5.09867 | -47.51035 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5c0151d6-23e0-3d44-97df-6ebb8c710133 | -6.98946 | -42.20009 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6d3ecd0a-4f2c-31db-8c14-90dcd2f4ec95 | -5.9244 | -42.68148 | 2026-09-20 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6a44d402-5e22-3e58-8e31-758155eee1a0 | -2.9107 | -57.79938 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9408fd50-bea3-346f-a66d-f66d330c5d92 | -1.74011 | -54.9315 | 2026-09-20 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2f8b3c0-3d97-35ba-890f-eec2b74f2915 | -5.6377 | -43.37981 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f938fedd-587f-34d2-8ecd-c1f71bc6ebe5 | -3.0208 | -51.19437 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 006e9ae0-13d0-3547-9b26-69ab36d40ad4 | -4.76728 | -39.5809 | 2026-09-20 04:38:00 | NOAA-20 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fb05184-a729-322e-b672-a46fb4770db3 | -6.17809 | -47.49263 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd1c8666-8a84-34fb-a111-6fa683ee6699 | -3.0062 | -54.17562 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0879185-7134-3b72-a4c0-b4b5fdb40df5 | -3.13111 | -44.47615 | 2026-09-20 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
