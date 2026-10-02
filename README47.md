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
| 47da3993-0e30-3560-b52f-2aa953b9c6f8 | -12.17253 | -44.65742 | 2026-10-02 04:17:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fde171fd-877f-3fe5-a450-c0cfe072530f | -11.66135 | -43.51182 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 511856e3-d507-3222-8765-9baa20d70a5c | -11.13259 | -44.62334 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a77fcae-9968-3b16-acd7-2fabd4269117 | -11.83965 | -45.01477 | 2026-10-02 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a463d5b-7c95-37b1-b41e-f74270ad6c98 | -11.69032 | -43.6073 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 027c2db7-7dd3-32bd-ac04-ae72cfaf3f3a | -11.13434 | -44.58929 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa4f2e29-87a9-32c4-bf41-441629b344bc | -15.2453 | -46.16541 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e74f6c5-1bf0-3e26-9ef8-724ff9d9a246 | -14.04379 | -43.84817 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de786288-17da-338c-b2ce-f0828ed01ceb | -11.74562 | -43.57978 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d8f00d34-41f4-315c-8727-cea175fe1c76 | -10.82614 | -51.09641 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0aa49a1c-1469-3572-a649-df336a9f80dd | -15.77066 | -43.64615 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f16754-0763-367f-99b3-d501e17d82df | -11.30824 | -43.5732 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50026079-e48f-3bed-b7f4-370031247a4c | -14.33445 | -44.74165 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24d4df61-ab27-3261-a868-d0bfe186c968 | -16.237 | -42.98347 | 2026-10-02 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba2924a9-2557-32b5-80ba-04668331c8a5 | -11.79164 | -43.56912 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4537260-f2ec-3ae8-9780-3e0362a1e703 | -11.4641 | -43.42839 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 039b24d1-1ba1-3f5f-aa71-5fa8193cb1a3 | -11.47462 | -43.42651 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da20983b-47a6-35ec-99d5-297e1f380de1 | -17.10239 | -41.92324 | 2026-10-02 04:17:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ba013b8-3bb1-3205-b341-2b434ce177b3 | -11.65604 | -43.58715 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d4acd0-fd52-3e0e-972d-4c02b7a8fa21 | -9.87052 | -48.22917 | 2026-10-02 04:17:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86112903-fbc1-3cb0-a9be-6932c0b5624d | -10.82668 | -51.09349 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e2ca5df3-39cc-3a91-a653-6c4221295efb | -10.2456 | -44.57477 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba5bad50-c0fc-3488-9ad8-3b8a7440418c | -11.72745 | -43.43942 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6aaa0a0-8ae8-3bda-a44b-55719ea33f25 | -11.44703 | -43.40749 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46c36b0b-9cd3-337b-9a15-479fbd64cda7 | -10.76191 | -47.7107 | 2026-10-02 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 257e5bc1-5a4c-3df9-b350-58fc0aefa34d | -13.34206 | -43.85866 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1a2abfe-cfa1-35cb-9c32-ce98e634a103 | -11.76004 | -43.57489 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f0b09fa2-d4f6-340d-bb5c-49dedab26f64 | -13.48073 | -42.48581 | 2026-10-02 04:17:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5eaf30d3-de7b-3f0e-ad5f-041a96317fbc | -12.9996 | -51.31236 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca3cf5c5-1296-374a-942a-c078b495709a | -11.74291 | -43.44921 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e641daa8-84cc-3d35-9327-df168d344fde | -11.67978 | -43.60919 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efbeb631-0908-32ff-b770-feeb266af12d | -11.14518 | -49.04782 | 2026-10-02 04:17:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b8926bf-2eb4-3fe5-9dc3-b278b7651c63 | -11.69364 | -43.60786 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e0d8297-599e-3657-8547-4f6e6eefb0df | -12.99366 | -51.27721 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 72b490d7-8738-30bd-815e-2d13dcb87140 | -11.44978 | -43.41156 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 584ebe09-f6b5-3946-ad4e-aa4e31c9d896 | -11.7045 | -43.51896 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab42e5ae-6e04-3791-bc51-065067f91238 | -12.66527 | -45.09745 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab085faf-29b7-32f6-8cc5-21dff94d96da | -11.4274 | -43.40437 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b29f5758-2d8b-3111-88b5-a75fbae5f9cd | -14.50191 | -42.21994 | 2026-10-02 04:17:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9890da15-3443-30dd-a9ba-0cb6efcf9837 | -11.26223 | -44.25861 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f90feffc-7fc1-3d2f-80d8-50bc40f4144a | -11.72138 | -43.4348 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe752f71-238a-3a1c-a022-0a2de063835e | -13.86299 | -43.63999 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 84aefbce-7692-363f-826d-ca57306615d8 | -11.46904 | -43.44006 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67908a49-2cd4-3c12-a1ba-2eab5af68f28 | -11.25086 | -45.2072 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 824ff4b9-2d5b-30a1-a8a7-99c7fdfd9f5f | -12.53047 | -43.09057 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0c7e396-b663-32b4-8c12-2d7bfe08e975 | -11.13289 | -44.61974 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6335c53-e8bc-365e-8b75-fb1a57de0f02 | -14.34295 | -44.73181 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b249d3-2dad-3000-b862-b2e1f3f7c9f2 | -12.93549 | -38.64854 | 2026-10-02 04:17:00 | NOAA-20 | ITAPARICA | BAHIA | Brasil | 2916104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8acecff-4f93-34c1-ae78-14d4a053d92e | -11.79108 | -43.57264 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11c8aee4-b184-38f9-99d3-58e5a7d7b527 | -10.78279 | -47.63836 | 2026-10-02 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbcb3941-66c6-3af4-8c77-2206c47a1160 | -10.30323 | -44.65059 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65a4df62-c0d3-38e8-84ba-3f47cd09db32 | -11.66649 | -43.60702 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d25f5f14-2ec1-361b-86ac-dbc17ba402ca | -11.70118 | -43.51841 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24cfbf4e-97a2-3d8d-ad17-a24353405e53 | -11.77998 | -43.57807 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88394e9f-1d1c-3113-bafd-fc05ee621d02 | -10.30448 | -44.64302 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b9d561a-093e-3767-b0e7-924973ab0347 | -11.73954 | -43.57516 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10b0bc48-b740-37fe-a494-5060a02bd1e6 | -11.76336 | -43.57542 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5dd6eff7-6dd0-319c-994d-434f4f277943 | -16.24034 | -42.98402 | 2026-10-02 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ba7e1a-5edd-3929-9bfe-1d5f0e208bd4 | -12.52388 | -43.06781 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed471aaf-93ec-35be-9f05-7c71dbb633ab | -11.65158 | -43.59368 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c151ca91-75ec-31fe-b09b-bc89ad748817 | -13.3354 | -43.96349 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 033395f6-4d1c-3137-8943-bdb4acb3413e | -14.87361 | -40.69644 | 2026-10-02 04:17:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6b8c8df7-3756-3179-994a-1365cf029cff | -11.71863 | -43.43073 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a662249c-6278-3746-9d46-3fe18805869c | -17.70855 | -39.76074 | 2026-10-02 04:17:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5286f009-c366-3a31-b867-078cd416157f | -16.12085 | -42.22836 | 2026-10-02 04:17:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 314cca81-adaf-3d0b-b78a-be9ff7be7aea | -11.26817 | -43.57005 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca8335f6-a049-38da-95d4-7089c31bb9e0 | -11.38717 | -43.35796 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 239d0a20-b834-3754-a717-ff4256995cbc | -15.92226 | -43.52464 | 2026-10-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d0a1279-890b-3ca8-b5e5-d52f14d81a84 | -11.47066 | -43.4512 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3319e84d-3a55-315a-963c-512a45ac7a05 | -11.24657 | -44.24847 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a4cf011-3098-37d8-8955-56e93816e8e7 | -11.76459 | -43.54665 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbda4795-9620-3779-a1ea-5086d4101909 | -11.15429 | -44.61927 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 597bd69c-3107-3341-94e1-0d99e13107a8 | -16.99894 | -41.18469 | 2026-10-02 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a2ec21a-ec34-3236-b14a-533ca3cf1c12 | -11.1515 | -44.61496 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d13a123d-eae4-3ec7-a4d8-767c4242c683 | -11.21555 | -44.84155 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a936dded-42d0-3eff-a7ed-6649902d307d | -11.39035 | -43.40188 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aab6bd3-4fba-31ca-b1d6-703637cae8b8 | -12.4655 | -44.15259 | 2026-10-02 04:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e742ffb-989f-3ddc-918e-49806923f167 | -11.6848 | -43.59917 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bedc4c29-2dd5-31d8-a6de-c78fea8239d3 | -11.441 | -43.52962 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8348c17f-8fda-3553-9490-c97dbb7c643d | -10.25186 | -49.67263 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 811c13d0-451c-3e17-ab07-98ad0ce14c5c | -10.24779 | -44.58292 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f72a6ea2-22a7-3a36-8524-7c0bba23df60 | -11.65044 | -43.60076 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b89dd4eb-18fe-3641-9b47-e2621341565a | -11.65101 | -43.59722 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b00264-a493-3cc9-a487-c73cac2b3cc5 | -11.60237 | -43.54211 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbfe84b0-de95-3635-a85b-43c8d5d839ec | -11.83859 | -45.04221 | 2026-10-02 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e91f8a-6b86-37bb-aa54-850404b2f3b6 | -14.48912 | -41.84202 | 2026-10-02 04:17:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d3d5bb1-168e-38f0-8b8e-45455ec0bd7b | -11.39698 | -43.40297 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1a03737-4ab0-3f52-99d3-db64b95c3ce1 | -15.16056 | -44.0243 | 2026-10-02 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b14effd-f307-375b-a76a-e61c1b9c0f54 | -13.4023 | -43.993 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3734d02-7b72-3572-845d-d595492aa95f | -11.78387 | -43.57509 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e7afacf-b3bd-38d7-bccc-950932701560 | -11.66316 | -43.60648 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fc35a35c-4473-382e-a220-50d85a63b2e8 | -11.10588 | -44.59216 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88d8c165-b3a4-3efc-8ef7-9a416e664346 | -11.78669 | -43.55754 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8911d64-f9d2-3736-b9f0-a5b04757306f | -15.31134 | -42.78246 | 2026-10-02 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab16c02b-b0fc-3877-8d80-bc3b2d51225e | -11.1279 | -44.60734 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b32700e-f57a-3a9d-ae20-26b4333382ed | -11.68742 | -43.498 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc79cad3-4b1a-3b3d-b332-20be8a18f988 | -10.897 | -43.8493 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6af9c3c-3132-3bf2-8971-4cb845648631 | -11.14809 | -44.6144 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| c6a08477-e1b6-3720-be88-21768abd16d2 | -12.51775 | -43.10656 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 277aaace-d1c2-3ed7-b440-60b61eb42300 | -11.64789 | -43.55313 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |


[Clique aqui para ver as próximas entradas](README48.md)
