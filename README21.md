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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9352e32-20be-353e-b29c-3e0dbe653e73 | -10.88388 | -48.0378 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09b97b0-a6ea-3aa2-80a0-b5f9041605da | -10.86945 | -48.04565 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0de25468-9d5e-3a4e-b9ec-f59cdf9bfd64 | -12.57799 | -47.34558 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2da63ca9-7ebc-3d89-a612-84d93cdf13d4 | -10.65079 | -48.0626 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 604c2b97-b861-3f71-8466-7946082fc1fc | -12.64206 | -44.30436 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e923add-e4fc-34d4-a7e0-00602093e9a0 | -13.35915 | -47.42292 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48116998-9a28-34a7-9250-614f07c0249f | -14.53581 | -48.04323 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186c0110-f599-3003-a82e-fbf56ecd2c81 | -10.87643 | -45.08338 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ceb50eb-f12e-3d2b-a309-9e2f109a920b | -10.89422 | -48.03903 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1598b976-f1e2-30a0-be79-3f2edd7ea3f8 | -12.77448 | -47.37262 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 638e1bd4-e76a-384e-a511-a2028e0f1e8f | -13.91012 | -48.41169 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 183e0d41-4ac1-3da6-bd8a-b05755682d99 | -12.09006 | -46.42158 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 090898f3-af8e-3a84-9a9b-f995cde8696a | -12.06275 | -43.9912 | 2025-10-25 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3c908d5-ff08-3ce2-8785-dd6646e2cb05 | -9.99903 | -47.10801 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 763851df-1e55-336e-9d54-2e5a1756dc40 | -12.80103 | -48.67504 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb2301ef-1dc5-3f42-8391-74924e967b52 | -12.04947 | -46.40512 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfb0848f-a597-3605-a897-3043a2505aa7 | -15.19322 | -44.07405 | 2025-10-25 04:00:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5ae7dd5-413d-3e45-9155-35c8191b96bd | -14.72072 | -46.61514 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb52d862-13a3-3f9a-9920-64d4f478e2f6 | -13.89525 | -48.40888 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3198ac8d-3436-3bdb-a44e-a84454b933a0 | -11.97648 | -44.96791 | 2025-10-25 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4245d9-6990-3551-8d96-744b71f9628f | -12.94461 | -48.50146 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81faf792-3e4a-3b4b-a21e-c03c51f925d8 | -14.86785 | -48.07971 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc0be92d-b321-367f-a802-9562a1f173c0 | -12.24111 | -47.49099 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 138aa6e1-b45f-3e39-a6af-0daecc8bf0ec | -14.87039 | -48.09195 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba668fee-1166-31b1-b8f8-ce929dd66600 | -10.83332 | -47.62568 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b72b2078-da07-31e1-aacf-aa5f3f80f9e6 | -12.14783 | -48.01852 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfc7eb0f-61ea-3b7f-a07f-9629e8feaeec | -10.63864 | -45.23362 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f26f3c-aed2-3ce7-a1d2-1074184aa217 | -12.05892 | -43.99046 | 2025-10-25 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d9dd2eb-4da9-3838-a2e4-0b79f0851536 | -10.27335 | -43.87232 | 2025-10-25 04:00:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5eb9760-f9a3-396d-b9c5-dc139d5acb11 | -12.47983 | -42.77084 | 2025-10-25 04:00:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 304e76ed-b21d-3cfe-8145-7ee1a1d67a6a | -10.95441 | -50.294 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e74292-7746-3694-9de6-951e8707a92a | -12.20902 | -46.51384 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 513fb23f-0d67-3a38-a9c1-4fe4f0fbc74f | -12.04994 | -46.4285 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ec14cc1-95b1-30b2-9c7c-c096c8a42b43 | -13.35536 | -47.41718 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05ee1c46-a457-3068-989a-d2040ec49f8c | -9.0867 | -47.81111 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 864b00f8-59ca-3054-9ee6-1e11db822d93 | -14.47409 | -47.9019 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16edb1f8-6cdc-321d-a7f0-3a6bf05fd55c | -13.31047 | -47.44937 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 885e2675-ca0d-3a9e-bd4f-db816959d648 | -11.42867 | -44.67788 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94c5d3ed-3826-328e-9283-0ed0ba0f350f | -8.87068 | -48.28935 | 2025-10-25 04:00:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f7b23d6-c987-352d-bb84-d03c0be3282a | -9.61035 | -46.89859 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91e033e4-63fb-3bbe-bab6-501f721254da | -10.44689 | -44.9663 | 2025-10-25 04:00:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 918e450f-02ae-3063-9553-7de89a2b0541 | -10.02483 | -45.00004 | 2025-10-25 04:00:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88494385-7fac-386d-b68f-51b391610b64 | -10.41301 | -44.74382 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaa9c465-cd5d-39cc-91e3-545f28f16891 | -10.45109 | -44.96698 | 2025-10-25 04:00:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e05b2da3-8854-338c-b73c-cff25307a0ed | -12.11603 | -46.71337 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92265d7b-4762-3e27-aa75-0e3f22c6e370 | -12.83593 | -48.63866 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1147a748-ec4a-3e18-8cc1-c0d2840f8090 | -14.19925 | -44.80606 | 2025-10-25 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27ce8c16-56f2-3358-b4ff-456e385f8abc | -12.12516 | -46.71512 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a5d44b9-70c0-30e4-9249-1209c6a700b4 | -10.418 | -44.5051 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74c2ad01-3662-38d2-9243-dd6588d97a27 | -12.79586 | -48.67421 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 197dc9b2-d34f-3ede-8317-71bd11f71670 | -13.54849 | -47.56789 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da2f7f6a-13be-3e91-b243-596dd7372dd3 | -14.86371 | -48.10488 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f94269ea-4a47-3157-afd3-afe2cbc25ee6 | -10.80453 | -49.65215 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c09a718e-d56e-3ed0-a1b0-6415bc28dee0 | -11.54681 | -43.1531 | 2025-10-25 04:00:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ca4aefd-75df-37c0-a10c-bb8188279bef | -14.44051 | -48.07373 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| becc3cfb-8e1d-3133-b7aa-b17e05d2f5a9 | -10.62454 | -52.19164 | 2025-10-25 04:00:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7437b9d-e16e-35b2-a10a-af7800adfe7c | -13.88034 | -48.40623 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8bea9ef-8965-3355-99f2-9590ee2c2aa1 | -11.75402 | -44.65249 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5232f021-b097-3266-b697-3f1bb2cb8f3a | -10.79429 | -44.91534 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8642cf-f9db-3e61-8ace-9a9ac144be6f | -10.87216 | -48.04383 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db24d6a8-9c26-3189-955b-e683c6500295 | -12.06133 | -46.40146 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b91e462-68f5-370a-991d-7374a084394e | -12.30543 | -45.52191 | 2025-10-25 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebb2ca64-7846-3c55-a74d-67607c0b70cf | -10.88115 | -45.08141 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a690281e-e76e-309f-ae2a-88b122112e7f | -13.25761 | -47.88808 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc45c71b-3f2c-3a7d-b256-1c206a2a0461 | -9.61522 | -46.89929 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60d2999e-eb36-3b77-8ce9-a055a8d31759 | -14.34063 | -43.73707 | 2025-10-25 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ff30e83c-82ff-3ef1-947b-6645a5dcfb5e | -14.38196 | -51.52961 | 2025-10-25 04:00:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a34b537-3e48-339f-8818-b00afc439a94 | -12.07467 | -46.40446 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fccd9f40-f61b-32a0-b670-1f5b2107dedb | -11.50225 | -44.00566 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eac6d57-acc7-33e7-9366-4be1bf06ad7a | -10.79885 | -49.65104 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b9dc019-f7f4-3ce6-b2f1-0a91443f681d | -14.54488 | -48.02141 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 312a3ac0-96a7-3c3a-b1c1-38f6041bf209 | -12.2373 | -47.4847 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d497ed6-9762-32b4-87cc-9adb73d0d201 | -14.87369 | -48.07813 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43b3746d-a3ba-3ef7-9ed9-560e52d528a6 | -13.20519 | -44.10741 | 2025-10-25 04:00:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f30a9255-b433-33fd-b921-2955593f181e | -10.42332 | -44.49853 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c4006f-43a5-3960-a347-3661c526f516 | -12.30094 | -47.45872 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4fff6d5-7edc-3186-9a64-fe212c4ae1aa | -9.75042 | -47.8367 | 2025-10-25 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a448c704-22ce-3053-bf2d-8713793bab60 | -10.87932 | -48.03399 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf5fd074-a38a-3cb1-824d-39711c64f71a | -9.18947 | -47.74644 | 2025-10-25 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b1dcb07-d4b7-3b7e-9c3a-bf37e26db33b | -12.12972 | -46.71606 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c05f162e-92ac-38c0-9ba0-e8ef83937c21 | -11.84568 | -49.86325 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eacd27c-5c2c-35a2-a3fc-68cdb734800a | -13.5438 | -47.56685 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75791458-8708-3381-9d4d-02cd075619b0 | -9.19002 | -47.74341 | 2025-10-25 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8faf78d0-d315-3601-a044-741c4e65d30b | -12.05163 | -46.40377 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbfe65b2-1795-33f9-ab65-2dd76f7ab5ba | -14.86683 | -48.08834 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 56bdce5e-e41a-38eb-ba80-bd10cad483fb | -11.7828 | -47.55049 | 2025-10-25 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fc8d923-3140-3411-bed3-ce373d513242 | -10.62269 | -52.18535 | 2025-10-25 04:00:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79ce9127-0104-3b93-873b-89e2bcc906f8 | -11.77693 | -47.55502 | 2025-10-25 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4cb0526e-572a-3995-9fc8-a095c38c6cbe | -10.6284 | -47.92628 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca62eea-6f7a-3450-80eb-d09592f15216 | -9.57528 | -49.67801 | 2025-10-25 04:00:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b0cbb82-b52b-3143-b5da-f8d6cc5cea8f | -10.87877 | -48.03691 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a91507-3ad0-308a-80fc-f24646ebabe4 | -14.5256 | -47.94105 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e262bd4-53a5-3ac6-b9d4-d96c95a7d366 | -14.45904 | -47.92851 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 887dd87e-0cb3-3908-83ac-7cf928a8cc30 | -14.86096 | -48.0896 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1c400e6a-8e0a-3b19-af86-3fba9d016918 | -10.88168 | -48.0366 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9a8026f-980d-3aff-9c7c-05118c4ed8e1 | -10.00075 | -47.59658 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83da9273-625b-37bd-ad7c-169f61b41fb9 | -14.89878 | -47.87229 | 2025-10-25 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ebd100a-be9e-3dbe-9928-6d69feab3bc7 | -15.01542 | -46.20377 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62af082d-2e20-319a-ab0f-363c548fcd30 | -14.38606 | -51.54004 | 2025-10-25 04:00:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 305d751a-eb9a-3b95-ac67-faf715f71a87 | -13.3313 | -47.93866 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
