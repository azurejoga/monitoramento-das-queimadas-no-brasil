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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b498bf-f35b-3daa-884c-6f9638f9eb8c | -2.27804 | -46.81044 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 138a5c78-e991-3118-ad00-99dfebdf60bc | -2.27335 | -46.71124 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 639d1f91-f06c-363b-b489-33c885f8ac38 | -2.27194 | -46.70138 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8d518fb6-9dd0-39fe-a757-9ba0793b0ffb | -2.27106 | -46.76166 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 42010d41-fde4-313e-a214-c8ae4f108188 | -2.25696 | -46.66321 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 148462c6-f889-3450-a13e-7153085d8c34 | -2.2507 | -46.80081 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 29426f7d-654e-3329-9101-1cc82a900587 | -2.24325 | -46.61069 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74405b50-9c49-3470-b863-7ffcf8340d39 | -2.22627 | -46.69408 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 93fed504-8cee-398f-a0d5-d202d9ccc624 | -2.22458 | -46.88388 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2405409c-eed7-3619-ba91-18cf4ee9de9f | -2.2232 | -46.87414 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3c5a2b8c-8979-3942-bde0-aedc04b0b68e | -2.2213 | -46.52174 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b9753785-37f1-30f0-a235-d9b2160fa36e | -2.1745 | -46.73165 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5689e0a-b9f7-387c-bcd7-5bf63c50115d | -2.44568 | -46.35727 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 289f471e-1780-3b96-a17f-546b8b79a83f | -2.44424 | -46.34706 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 21f877fc-7506-3104-8161-a96dae323a06 | -2.38327 | -46.5682 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b72f67b6-7a7f-3724-8217-9fc0bebb6c4c | -2.37479 | -46.50806 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e996995-aea5-356b-8d41-f22672d28b32 | -2.37389 | -46.56953 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34bcc9b5-dc58-3e0f-8219-c8d23f40de84 | -2.36538 | -46.50939 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f7d5b203-03fa-3d93-b15b-6e63f2c7c16d | -2.35025 | -46.47044 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| deacfee6-349a-347d-a9eb-690c71ec1213 | -2.34881 | -46.46032 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5799ef06-5f2b-3e01-a4a4-be6cce582e98 | -2.32303 | -46.52141 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 820835c8-ae5f-305c-98bd-58495d5a23d6 | -2.32163 | -46.51136 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dfd0d577-a595-340b-9617-d3d09ee9e5e5 | -2.31222 | -46.5127 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 14799381-1ca7-3b56-ac76-7ff0b812855c | -2.28772 | -46.47504 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eec770dc-4288-3de4-ab57-42b2f87280fc | -2.27686 | -46.46628 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1b77712-a7c9-3e75-986f-02d096a845dd | -2.2199 | -46.51165 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4b98ca67-bb4a-3b03-b0ae-4b837dc70a64 | -2.20482 | -46.47256 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| e746c642-c84a-30e3-8b0e-851b80152000 | -2.2034 | -46.46241 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 6a33ded8-4886-3fe2-80d9-045788f44d56 | -2.19537 | -46.47393 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 37aedcc2-8213-3111-8e2d-3937c9d1577b | -2.19395 | -46.46378 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 9cae3efb-65b4-35a0-a90b-b81e39aabb04 | -3.50077 | -46.06921 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f5e7a9b2-8eb0-3d86-bd47-195e5ad18db3 | -3.49929 | -46.05887 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e4c0a751-821e-3392-9c05-9ba463240d59 | -3.43817 | -46.20977 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2416aaf0-1fe9-32b5-bdb7-52d20400387c | -3.39878 | -46.06919 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0d692fcf-2298-3e71-8a70-27e01f237aed | -3.36224 | -46.04872 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e14cbfd0-56b6-3752-94a7-ba2266f4401a | -3.3527 | -46.05014 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c83635d4-9450-36ee-9934-98ff34073565 | -3.26874 | -46.24641 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 947721b6-9088-3c37-8f18-b7ae04e0b36c | -3.22367 | -46.20098 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da16f8cd-e7ef-3a55-b9c8-b34d1d9576e3 | -3.22221 | -46.1908 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bff11d08-1fc0-3590-aba9-0fe13a1f6dc1 | -3.21419 | -46.20232 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 95ee976a-c871-378b-9b52-9d0090e06915 | -3.21125 | -46.18191 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a00161a9-8a5b-34f1-be85-a3438dae929a | -3.20978 | -46.17169 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 74996664-56cf-3b8b-8cb4-2155f5b76ebf | -2.60638 | -45.98144 | 2024-11-02 00:54:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| efbf2169-cf22-3306-b7a2-57679cfe5c96 | -2.59978 | -46.14397 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9526d6b8-bc80-3592-8fe9-969f877e1e3f | -2.5902 | -46.14533 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2abcee60-77d6-3c5c-8972-a87f957e96c6 | -2.56804 | -46.12713 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| aa3c3854-3624-3e5b-a121-285aac153ed1 | -2.56655 | -46.11671 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7b5b19c1-c6f2-3a60-873e-8ef5a81516b6 | -2.49327 | -46.11201 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ab05e5cc-eeb4-34fb-9162-c29ff4b05c32 | -2.46747 | -46.13718 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f531f15a-ec7f-3cad-88b8-3038eba309b4 | -2.82361 | -46.62576 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 1c445313-876e-3c9b-b1cc-4f13973b5325 | -2.82221 | -46.61593 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 541cf80e-586c-345a-9130-e8477fcb6718 | -2.70735 | -46.70461 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d73dfb51-df0c-3ae2-b8bc-fccbf3f85c0f | -2.68773 | -46.76704 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e74617b7-e661-3042-830b-366f88973b18 | -2.68637 | -46.75734 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6189f884-f927-3b09-89e3-58e6a1b18bba | -2.685 | -46.74763 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2ae3cbd3-66a4-3c67-ac43-0f5b7e1aa06d | -2.67711 | -46.75868 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab751823-dce8-321f-9007-8bb63b39f0c0 | -2.67574 | -46.74897 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 712a7e25-2b65-39d4-99e2-e05125ed0f0e | -2.67436 | -46.73925 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 80a3ecb5-5881-3a4f-b62c-89a187ac0165 | -2.67298 | -46.72948 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d3865fd7-040d-3891-b7e1-11e339bcc489 | -2.55354 | -47.32044 | 2024-11-02 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e70977d-aab8-3b5a-b23a-4d40682a7231 | -2.42004 | -46.69434 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 777fadaa-1851-3199-b4a8-bf7c26573ed6 | -2.40832 | -46.74604 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 68c3bec2-bf0e-3320-9e13-c64d05bfd636 | -2.40694 | -46.73626 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 59a82a46-faa7-3c48-a632-d57fe4670a9a | -2.39765 | -46.73762 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 56aee01a-cb3e-3081-93d7-fdafaeddd644 | -2.38697 | -46.72917 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ddb06532-06ee-3c94-bf94-37ba8a811db0 | -2.37025 | -46.81126 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e3ffd076-70e0-3af2-b955-786c88cc7126 | -2.33691 | -46.62141 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0372df37-312a-330d-9874-8db0070b717e | -2.32893 | -46.63269 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c5d6e2e-e979-382b-b674-9aaf587783dd | -2.32132 | -46.7144 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6886e0fa-7b46-3a45-982e-5dfaf0931863 | -2.30784 | -46.68617 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df3ff84c-8ffa-33d4-9843-9cc143cabdfc | -2.30073 | -46.83701 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba24d2ee-03d1-3708-b372-6d59b360aa9f | -2.29935 | -46.8273 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 180a5a89-5b80-3187-9fb0-318db3a27631 | -2.28035 | -46.76033 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2bc83361-08be-3c35-ab3e-a23987cc499b | -2.27665 | -46.80072 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c3d996a0-90ba-34c3-9817-10feed945d65 | -2.25837 | -46.6731 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7dbb3f0e-cec6-3131-8f40-464e51e822d4 | -2.25367 | -46.88958 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a2dc242d-05f0-32d7-a031-3d868338cfe4 | -2.25152 | -46.67032 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 95e3675c-8a87-3122-977b-38d826393477 | -2.25014 | -46.6604 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7295d66a-39da-3740-a0cb-345af3200de6 | -2.24984 | -46.61355 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 258979cb-a292-3de5-a2ae-19b550f40433 | -2.24141 | -46.80211 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 876ac101-a16c-3acf-aa4e-704b68278896 | -2.17309 | -46.7218 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 80474f15-b794-3cab-8374-4917a25c1e99 | -2.16755 | -46.72847 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d75c2ce9-b537-30c5-8689-957025e0e97f | -4.31088 | -46.90585 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d25bb20-58cb-3dff-8d79-f07ecdf470c4 | -4.30181 | -46.90717 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7864cde5-bf48-3ba1-9712-82c60c6217b6 | -4.25892 | -46.86566 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5890aca9-72d7-3a56-bcb3-c2e3b1cfea69 | -4.2576 | -46.85636 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 07b91d9d-1d66-34d9-a191-261c1408e9ac | -4.25555 | -46.39217 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| dc5a942b-a2c3-3c07-9b14-0b8134337721 | -4.25414 | -46.38234 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bd8fa283-e2a8-3b67-82ad-de5880ff558d | -4.19966 | -46.71094 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aa044a6b-f175-3820-9d03-b34adac503f2 | -4.1983 | -46.70145 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a45ab8af-da03-3f34-9e4d-2554462973fd | -4.19694 | -46.69195 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b1e1f750-622b-38fd-925e-28a6c5744c7c | -4.19532 | -46.80437 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 956b9c82-2e81-3292-903a-80af8cf808ed | -4.11081 | -46.60307 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6095c00-f761-3392-a393-c22d13a274ef | -4.11009 | -47.11681 | 2024-11-02 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 92a89efc-9d22-325e-b58e-e8ecad538ce4 | -4.10944 | -46.59345 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 23378a01-6dd5-3014-9d98-60cd5f835e20 | -4.05672 | -46.93567 | 2024-11-02 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e9399daf-ff19-3c72-9462-d3252a155088 | -3.99779 | -46.45761 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10af172e-eb56-3daa-8727-e8c4812f432e | -3.98992 | -46.46871 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7aa51127-0f6d-38ab-860c-6a187de7fd85 | -3.98854 | -46.45909 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 0ff16203-3610-37a0-8f74-3874cc8f2200 | -3.92789 | -46.41404 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README11.md)
