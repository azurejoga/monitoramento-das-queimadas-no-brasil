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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b396cb20-0040-3a39-8a70-113dc5852c6c | -14.6147 | -48.40389 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a4cb8b9-0b93-3876-b75e-424df0d1433d | -19.03364 | -42.02749 | 2025-10-28 04:17:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6599f0e8-ccc8-3876-9b26-5644b2465a7a | -13.88704 | -48.50297 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c990c53f-8a27-3bf6-9ce2-02bfcdd60916 | -13.42423 | -47.37688 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 500bdbdd-5296-3988-9d28-341f6980e1ab | -13.31755 | -47.69077 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9794c93-ff61-3cf6-9825-eb31e12d6278 | -19.25265 | -43.66282 | 2025-10-28 04:17:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f4b9d50-8b6e-39b7-a91a-6b24358dd756 | -13.77819 | -44.36489 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1731d2b-a3e3-34a4-87fb-d7a68e07b749 | -13.65615 | -47.63806 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd4850c7-7eb8-3daa-ac7b-5112f22cec2a | -13.78479 | -44.36597 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b2d23da-64ce-321f-8837-26f678bd42d2 | -19.0262 | -42.02637 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d80031c6-dcbc-331f-b954-cbc5e52c565b | -13.7404 | -48.4332 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0398b83-7e0d-34db-8e88-ba11e9cd4b1a | -14.53662 | -48.00049 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e16ebfa7-c4b3-34bd-bc78-45b993792277 | -13.57845 | -48.52876 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca89a6ee-0d97-3b6d-9ac7-2ecd1d728d93 | -14.7244 | -47.36149 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 814ef9c8-ff1b-3210-b9ae-e65909e07f30 | -13.90712 | -48.47477 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc98273d-f07d-32de-9789-fefd0d8ae77e | -14.72787 | -47.3621 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa48e518-7cec-3981-a46b-e7daf6d200f1 | -13.66116 | -47.63016 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b53f4afb-36dc-3b91-905d-d7fcb9f22366 | -13.86244 | -48.51277 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac356bff-c8a2-3ddd-8440-2718a89ab569 | -13.79028 | -48.49762 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ca8da2e-35a8-367c-9d25-12282eef51b3 | -13.91498 | -48.49569 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5a8d924-c70e-3239-8fa6-871264d4c49f | -18.78741 | -43.46236 | 2025-10-28 04:17:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 889c7b47-7a6d-3b42-8180-5121fdd50719 | -14.76597 | -46.60104 | 2025-10-28 04:17:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24ac28b5-3421-3627-bbbe-15fff75571f5 | -13.91811 | -48.47732 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c69cca65-51d0-320b-b1d4-e6f2419eb5e2 | -13.74074 | -48.40956 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11d5aa48-cb66-363e-aeb7-710060037db2 | -13.74251 | -48.40696 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fe0df40-3845-3fff-9a7b-fd74602e23d6 | -14.62434 | -48.41304 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc3e0ca1-537a-3331-9438-cb4e2c92d602 | -13.63566 | -46.46449 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8df86d2-d6f5-3b4f-9204-7e288ddfa088 | -13.77711 | -44.41542 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a541648-835e-31bb-a610-1b357b2bc140 | -13.63581 | -47.04005 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 77408c2f-00a4-3ef4-bbf0-73604d6e31c4 | -18.82069 | -43.22639 | 2025-10-28 04:17:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| be26bc3f-4a01-3c10-babe-a195224ff81f | -13.24495 | -47.05919 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c4b9795-082b-3522-aabd-7f99c91e8c45 | -13.67173 | -46.52115 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db748a40-4901-3d55-9df3-1cb2bb80e909 | -13.7866 | -48.49684 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c19c25f-33b2-306e-bd7c-161a4174233e | -13.21947 | -47.10424 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1938ac4-70a2-3866-8953-6b5251406684 | -14.40925 | -46.67648 | 2025-10-28 04:17:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7d86c59-5621-38b9-b25a-52ed9659d481 | -13.18784 | -48.44273 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2535ca13-13dd-3b21-8c36-7c251a8dec9d | -13.63165 | -46.46767 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a566d628-259a-3718-91b1-8e82c2e42fa6 | -13.39475 | -48.51661 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 014221e2-f8ab-3200-9720-22028d0dc5a3 | -19.30488 | -45.73959 | 2025-10-28 04:17:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a263529b-640e-31c6-9ebd-7ded04c50765 | -13.64616 | -47.61491 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1623d359-7f88-38cb-9162-a5362867fc27 | -13.31913 | -47.43984 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ba477714-b8f7-3fbb-b38b-78a2b9bd88f6 | -13.31198 | -47.69349 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e4e3c5d-ac97-397d-b06f-99fcc2320ee3 | -17.62595 | -43.99178 | 2025-10-28 04:17:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5628e01-612c-3eb5-a8ce-c75c83e5d190 | -14.3165 | -46.51373 | 2025-10-28 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80500448-942d-31df-92c4-984925ae8df0 | -13.93076 | -47.73645 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73842cef-8e63-3dd4-94ad-deea8ac1f832 | -13.62886 | -47.03898 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb2206a4-a766-3a25-b30f-87d801c4d068 | -13.6736 | -46.50981 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aab8e64-be63-3d3c-8875-893054b7b3a9 | -14.01405 | -43.82697 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f855fa60-347f-35a0-b632-7919f613702f | -13.88418 | -48.49743 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b31a8b73-2a09-3f28-a312-7239e7c27713 | -19.25552 | -43.66741 | 2025-10-28 04:17:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ee576db-1f98-39c2-9a04-4c8078dd2470 | -13.87601 | -48.50056 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d306a08-0899-3bd5-bcda-18f0e445f0a8 | -14.89517 | -46.75902 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5701765-351b-3579-a599-05ec592921e5 | -16.14365 | -45.09666 | 2025-10-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 968a347e-16cd-3ee6-a00d-4e24e59563fc | -13.74173 | -48.41154 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24fd4cd8-7b5d-3977-9e03-39b33b45e722 | -14.08288 | -44.15275 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09f7983f-875e-3655-983d-dedf3524f615 | -14.75773 | -44.95427 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62ecb3bd-8434-3f5a-b1c0-ed7a7ca24890 | -13.48349 | -47.45663 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d600efd-ce7d-3db2-9c92-f8b278355dd4 | -20.14069 | -42.41256 | 2025-10-28 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d24c706f-b475-3e40-9c23-386afac3bcf0 | -14.41857 | -47.85933 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b1bc93d-c878-3a42-a38a-ea0f3feaac3f | -14.44173 | -44.80033 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd1e2127-1e29-3b10-848d-cd6fc9e91d0e | -13.78289 | -48.49617 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7a558dd-c39c-37d0-9299-9a50227908c3 | -14.15059 | -45.32977 | 2025-10-28 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa4bd271-e7c7-3858-895c-7d4b69fee760 | -13.55927 | -49.59141 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26a85480-8f13-33dd-bd7d-c76b0e24ce02 | -13.5356 | -47.16949 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a6a9324-608d-3798-bdf4-1e12e19ffc07 | -16.68204 | -41.36873 | 2025-10-28 04:17:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 021538f5-fe77-3514-950d-13373c79cf75 | -13.55209 | -49.58579 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49f6f266-14a8-354d-9419-9c0eea11792c | -15.19644 | -47.21059 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b64086e3-9254-3492-9cb0-2bfba1605459 | -14.53375 | -47.99564 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1fa39bc-12ca-3b2a-99c1-ac8aa6b9508b | -13.2478 | -47.06362 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cf6929f-4fc3-3a2a-8030-6c8954af8faa | -13.86528 | -48.51836 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad208946-4b0e-3da1-a7f7-a5cfef30e38d | -13.94648 | -48.39993 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf7bc4b8-e2d8-3069-8beb-acf6531e50a8 | -13.88128 | -48.49215 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8261dbe0-7377-383d-a8ee-1f418d9addff | -14.62356 | -48.41752 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2358ded0-2dbf-381a-98c8-5f0d46915343 | -13.42776 | -47.37747 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e807102-cacb-3c95-bebe-ae6371004f27 | -16.54357 | -43.58389 | 2025-10-28 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8af2f239-29e2-3c0d-b2bb-4fe83f85fb75 | -13.62811 | -46.46352 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68bc987c-eb41-3120-a8ed-f63b68c599ae | -13.13408 | -48.24346 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0400b911-5c34-3ead-867f-2d08cff5cad6 | -15.19715 | -46.35505 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56ee4855-6262-36ee-9a5d-b3968fb80909 | -13.67049 | -46.52871 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 551ffa68-8243-34ed-a6ff-4ba426797861 | -13.31688 | -47.69478 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d242362-060e-37e5-8343-07788064e83c | -13.27885 | -47.97202 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01d3080e-bb91-3f2a-858b-914f5d8b3fb5 | -13.66833 | -46.52057 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abd8c068-4081-38f4-88d1-9481ee84c652 | -14.76322 | -44.96245 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9801e3a-b1bd-39f7-8e57-1eb58d50df9d | -14.62859 | -48.43187 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c2c467-37b8-311b-92f5-984653bf1323 | -15.7312 | -46.29573 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f485715-6985-368e-8d4c-b2d06ce94778 | -13.39935 | -47.35247 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cc1726e-844d-337c-bdd9-2a20977d1b5e | -15.74069 | -43.82143 | 2025-10-28 04:17:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b7deb0a6-3542-3454-b992-0f4432bf4bcf | -13.55936 | -47.15624 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01db1302-c36c-3935-8d0a-df2631799454 | -15.15563 | -46.58712 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 627206b9-3097-3396-8907-2ce8455088d8 | -13.37807 | -46.63958 | 2025-10-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 896aeb12-6cba-33f8-a3f0-380e9d9894d0 | -13.15418 | -48.21498 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fd1becf-53d2-3b75-ba18-3b28454bb3e1 | -13.25705 | -47.96416 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a88fcc16-a024-366d-958a-45bdeb286906 | -15.176 | -47.22702 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02538394-c48e-3ad1-9b0d-10493eb20f87 | -13.62951 | -47.03507 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7562340d-98ee-3c1f-81c8-35c28f03f6f5 | -13.53909 | -47.17009 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78af5348-fbe2-3c0e-be74-c2f7ad12e973 | -13.79193 | -44.34177 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e726b133-3904-3b5f-a191-b2f70ad9f1f7 | -14.08619 | -44.15328 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b7c6aa0-8a10-36f6-b75b-87839dd2e638 | -13.77987 | -44.46296 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e94fdaa-7d67-3d70-9a25-121e562fd017 | -13.18629 | -48.45189 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45e1ce9d-6d99-3d75-a016-7035ef5c2102 | -13.89067 | -48.504 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README42.md)
