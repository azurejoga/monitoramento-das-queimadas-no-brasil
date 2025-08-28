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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 628221a1-e081-3bde-88da-d877cf21069c | -8.08444 | -44.98262 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d14bee7-7c2c-3510-8bdc-4e17c5a5352c | -8.45593 | -43.65514 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9abd3516-fd9d-31fb-8e34-76a5ba4d8a4c | -6.24411 | -43.38061 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9579da1-00c9-305f-b7d8-69ad073f0bcd | -6.07805 | -43.99949 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0da0223-b2fc-3c98-a47e-3f32edeaa2c4 | -5.67195 | -39.07037 | 2025-08-28 03:45:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38025ff3-21b8-3c24-8103-7bb8b0454ffa | -6.18397 | -44.16566 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6378cb6-a9bb-31b0-ab52-f3ee1ebcd892 | -4.15538 | -43.88055 | 2025-08-28 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2036f635-a06f-3204-a265-7b8721b4147d | -6.1631 | -44.06602 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d29999c-5987-3a3b-a7ea-970058480415 | -6.88474 | -43.60655 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f000e5f1-eee7-366b-8e22-041fdedb2f39 | -5.77206 | -44.92611 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8bb38ec-3911-33aa-becf-685ca6ac3a66 | -7.31938 | -46.11017 | 2025-08-28 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1d65121-612d-3c01-8f25-2ba364b307ad | -4.67361 | -41.02355 | 2025-08-28 03:45:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47a6423d-0d1e-3e0f-a246-f8900914aef5 | -6.8713 | -43.62305 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c643f135-6408-3afd-856e-253bd89b948d | -9.13617 | -40.55795 | 2025-08-28 03:45:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e26845ca-154d-3c5b-b0ec-ba3e992fc52d | -13.53822 | -46.89103 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf83c827-4864-3852-9aee-3c0a39bf1d88 | -12.7957 | -48.15877 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5abf1e4-f774-39c8-89fe-eac791df1aba | -15.08257 | -48.63951 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f654001-4826-3ce2-8c3b-02b924742f90 | -13.67196 | -46.90847 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2447145-2549-34f9-b0de-45a2232aee33 | -13.42176 | -47.00348 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79fbe22b-a2f4-31db-9b15-482305bd8e79 | -13.6217 | -48.23469 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca161906-dd0d-39ed-9a4d-57355415cda3 | -13.55059 | -46.9034 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6895c5db-629f-377d-92a1-240c90a6299c | -21.60626 | -49.70148 | 2025-08-28 03:47:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11da360f-ff13-3e70-8efd-33eff0e38983 | -11.33319 | -43.5221 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18b786f2-f1c3-3141-b260-bb8a1752f310 | -13.6212 | -48.23906 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 958b7435-00b5-3413-b215-d2e65826d31b | -13.42935 | -46.98662 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c536eaec-af2f-33ab-abd5-2512dcd9f5d9 | -11.24416 | -44.98056 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a9dbfca-f7b3-3016-9d1a-71beb9501872 | -11.3454 | -43.53465 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a736a57e-464d-31b4-b015-4b3342e4148a | -20.11981 | -44.3457 | 2025-08-28 03:47:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5f323816-bc34-3dfd-81e3-f7b1ba240222 | -12.67828 | -48.17726 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7436fb6d-812f-3527-88f4-5d9fa35fcf64 | -11.65156 | -44.87722 | 2025-08-28 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f962693-3630-35da-ab0b-fd944e98948f | -20.72716 | -45.85467 | 2025-08-28 03:47:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a437fde-3069-386e-8da1-3045b48881ce | -15.7257 | -39.87889 | 2025-08-28 03:47:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 58a70963-1642-3e69-88b7-82e15783ea60 | -13.18682 | -45.29079 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38595ad2-0721-39e3-936c-73772d03ed2f | -13.52771 | -46.88528 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5fe748-7f97-3acc-b4c1-d477e6fa8417 | -13.67122 | -46.88272 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d09b72f-3d21-3e20-b554-d51933b93353 | -22.23307 | -42.28996 | 2025-08-28 03:47:00 | NPP-375D | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e326d19-2864-30d4-a026-a7c410b886d5 | -11.24508 | -45.00365 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c435a1da-e26e-347c-9b4a-f55ca9f6b8bc | -11.80674 | -46.81499 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b74ba7fb-4737-38f8-8ffa-4680a3ab8a95 | -11.32017 | -43.54016 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18af3ae3-a47f-3b74-a48f-477463cc41f9 | -12.68547 | -48.1735 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f277589f-5a4a-3e5a-9219-dd1d419dbc54 | -13.63737 | -48.22172 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23a15e72-25e9-382a-b82e-007d18434499 | -12.35522 | -38.27945 | 2025-08-28 03:47:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c6dab53-9636-3ce3-8935-49bab1db8495 | -11.25102 | -45.47654 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30999c10-ad15-3202-9afb-df87061cb276 | -13.18799 | -45.2847 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecf426f8-f266-3d49-a10a-922a40be6516 | -12.43862 | -48.71281 | 2025-08-28 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dacf699-8815-304e-91d0-15df79314919 | -12.69144 | -45.08621 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13015b33-90c1-320b-a386-5cdc5073c9e8 | -12.80911 | -48.12471 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63d55a8-6432-33eb-8ab9-99a5185eaffa | -13.60135 | -48.15052 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ea6d98-aac0-3cdd-ad83-e56c49b74f49 | -13.43256 | -46.97032 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 38c082a3-a47c-37ea-9f0a-ef91637de1e4 | -13.42283 | -46.98988 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8532e2e-5543-3ee2-846f-84443cab41d0 | -11.74498 | -49.08448 | 2025-08-28 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37f4dfab-a161-3d8a-82b9-ed7a1d1c1a79 | -12.95672 | -44.58604 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 42daf0c3-3e23-399d-af05-b1604d9963f5 | -21.6992 | -42.41832 | 2025-08-28 03:47:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 815f87bb-bb94-344c-acbb-90374cd1658b | -13.99393 | -46.34544 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22154a6a-bcf6-31bb-98f1-1fe9ce510802 | -19.2834 | -49.71451 | 2025-08-28 03:47:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ee64844-f415-37e6-9379-71c7af5b5948 | -16.37247 | -43.79454 | 2025-08-28 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb0b9784-c513-39d0-b36f-13cfd8d8face | -21.13071 | -44.21711 | 2025-08-28 03:47:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f791ad6a-15aa-3d08-855f-303b486a4fd3 | -12.78452 | -48.18184 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 766b3d91-acc7-3856-91a8-21eea6c00a73 | -16.36808 | -43.79387 | 2025-08-28 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32215e87-836f-3d76-8562-e99ecb424a9e | -10.37289 | -45.16727 | 2025-08-28 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1abc623f-856b-3c19-894c-5955b0a1cbeb | -13.59429 | -48.15417 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac15f0ff-3584-311d-972c-b51be01bce36 | -13.62621 | -48.21435 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72764c95-f8db-36f3-9461-37faf269b26d | -10.528 | -46.69413 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eac41d1f-ebb8-324f-a9f7-4b3b4cd8efac | -11.6465 | -44.87608 | 2025-08-28 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20fd87b4-2608-356d-947c-0a920d633af8 | -21.15031 | -42.44468 | 2025-08-28 03:47:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2cf128e2-eb62-39b6-9fba-dcf62c3e3834 | -15.0835 | -48.51655 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b27fe15-02c4-3ca3-b274-946c556c6cd2 | -13.55447 | -46.91293 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d994586-c7b0-39fb-b412-dff9fa3497c8 | -11.33421 | -43.54285 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 614b5181-5ee6-3725-8592-5d6ab1ace79a | -20.25242 | -42.00827 | 2025-08-28 03:47:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 6fc60868-c155-34c6-8f89-a4d6fcac02f1 | -11.25288 | -45.48005 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccba458b-2df9-3bab-8ff1-5c6629bc8cae | -12.7405 | -48.18657 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3093f2b0-6d63-3fba-a73d-5ca27a21cbcf | -21.14687 | -46.97305 | 2025-08-28 03:47:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a9bfcd-d63a-30cb-860b-f263b0ef1f0c | -13.42132 | -46.99753 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99d003d9-3f6f-37a4-8c59-330e91ed2dfe | -11.31549 | -43.53928 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dce2e8e-21dd-322f-bc8c-916e5c23e740 | -9.86471 | -44.68744 | 2025-08-28 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1367bc0d-fd80-3eac-9f72-6c93b38c07c2 | -12.8121 | -48.14122 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29cda41e-255f-35eb-9f6d-29f5f1013c47 | -13.98187 | -46.34154 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b662f1d0-30c3-3f38-89bb-d3871ac7ef97 | -13.45598 | -46.97992 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b248f77d-783f-3204-afd3-c16b9a17ea6e | -13.18232 | -45.28671 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8a87643-8755-3fd0-982f-72894243625d | -12.80701 | -48.16595 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f8436fc-0343-3e7c-a01a-e21c61ad2806 | -13.63194 | -48.24636 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 719c5b21-b34d-3dd4-9c75-6a5fd37bf97f | -12.95294 | -44.57938 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 091287f0-aed0-351a-a46a-2cb763a6479a | -12.67717 | -48.1826 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 406ec837-b286-399a-b797-cd5d537b11f9 | -20.43796 | -47.33704 | 2025-08-28 03:47:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 131a7aa6-134d-35a3-a87c-3566a9563d44 | -13.51947 | -46.92654 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f44e8e3b-c1a4-31da-9495-62712afa2bb5 | -11.34449 | -43.53964 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0b96c230-e71b-3be7-a3f2-2789d6e137e5 | -14.1314 | -45.40968 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 305e125d-2933-3583-9e3f-6dd356f4253f | -20.25051 | -42.00977 | 2025-08-28 03:47:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 787f4238-1fff-35b3-a370-c1dfe3e1ec26 | -13.42691 | -46.85143 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0606a0a3-2e2d-3306-847d-524ec6e3f1f1 | -10.32305 | -46.76902 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4427d78f-7471-3c7c-a778-5bdc2a202542 | -11.34072 | -43.53379 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4b2e3e92-8fc6-3df0-976f-4c7315464fb5 | -16.54576 | -42.34726 | 2025-08-28 03:47:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcd1076e-e3b0-3058-83da-2143546aa2ea | -13.55137 | -46.89959 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af1f60a4-e1ef-33af-974f-5d9543ec33cf | -13.59962 | -48.21918 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f0b43fd-825d-3a34-aa93-55f5d8348947 | -13.51257 | -46.87356 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4249f25d-de4d-3132-9970-eb3267a71c30 | -20.44843 | -41.9463 | 2025-08-28 03:47:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0385a726-7bb3-32c3-814a-ed09756214b4 | -11.33799 | -43.54867 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 78f6121e-1885-3343-a688-c37c25dbe9c3 | -10.53059 | -46.71206 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0031457c-ec1e-36c3-813d-1b28700c633e | -13.55535 | -46.90865 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a004a4a-9e15-3e46-86d5-3ad312390b2e | -13.46065 | -46.98587 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
