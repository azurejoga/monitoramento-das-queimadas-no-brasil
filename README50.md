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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d89099c-7795-35c6-a116-2295dff55345 | -5.68214 | -53.50011 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ba0ff6-8677-3f8a-9698-27530051cc2f | -7.72238 | -47.06141 | 2026-10-06 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89f6c937-a33a-3db9-bff3-79aca44aee26 | -7.81994 | -45.30786 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3ac0ba2-d0eb-330d-abd3-2141647fd11a | -11.67135 | -43.66552 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eb2366e-2455-3154-84fa-e3f02c55b81b | -6.4574 | -55.43125 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47e1af1c-aaca-37bc-b7c3-81b787dbb59e | -6.45077 | -55.43262 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce0ebdf3-57f4-3059-b7c5-fb4019806fe7 | -5.7504 | -46.68338 | 2026-10-06 04:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ffe1dae9-6dd2-3e27-9bbf-6eb40f74cfb3 | -6.98033 | -47.7414 | 2026-10-06 04:40:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 741f7615-263e-3f19-a585-cb2d04d1aa4c | -11.36496 | -46.68 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8861054-c7bc-3e8c-b091-156dabadfd25 | -7.24568 | -45.25599 | 2026-10-06 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efc743c4-9b98-3b3d-8784-0c3726568fab | -9.80278 | -44.7916 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e677411e-6448-3910-a27c-5ea6cd77c6d2 | -11.27272 | -45.51965 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 46dce041-b66d-35fa-8329-c74585387b4d | -6.17306 | -44.29049 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 654e9c6c-7bc0-3ca2-8f3e-35ce26b53596 | -6.32259 | -43.81473 | 2026-10-06 04:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01bcb805-b3a8-3090-a7ea-dd8b8de92cde | -6.46325 | -55.45317 | 2026-10-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bac3d2b4-f255-317f-bbfa-9dd17cf8a8e0 | -6.34779 | -42.54974 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bdb4d08e-ddf0-3e8e-8cec-af7e0b64056c | -4.28782 | -54.80623 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37fda818-1481-316e-8f31-83424647a4c4 | -11.82426 | -43.53079 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8968291e-b52d-35b3-89da-0aadacf581f3 | -6.4486 | -43.82743 | 2026-10-06 04:40:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd2ab331-02ac-338e-9991-9489675ac0cb | -11.82621 | -43.54819 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d70adffe-3d12-31da-875f-b2aa01872d22 | -8.58307 | -45.66589 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c66b39d-d558-3d2d-a10f-bda91e88fc89 | -11.75047 | -44.93686 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16a1a226-f1e2-3fe9-9888-39eb4a63880f | -9.79587 | -44.78588 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7d4c078-3a24-36e2-8020-cc2c31e423e9 | -11.23278 | -45.26265 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f83538-f706-345f-982d-f761668309e9 | -6.92773 | -43.67945 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfacce77-4006-317f-be54-e758d0c4dfa7 | -9.25509 | -45.65891 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c6289ed-8a86-3c06-937c-098f6b57721e | -4.46486 | -54.97137 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7c5753e-3cab-3512-9f08-1f10c3660aa2 | -11.28272 | -45.50294 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d386e588-a386-316d-ba65-3fad34804bb1 | -7.57133 | -46.63829 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32879005-e192-3b10-9e85-f773a87b2ff3 | -11.36031 | -46.68725 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ec0d7d-59ae-303e-b552-5e2f26dc9f2a | -6.36552 | -42.5445 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 41b3cf85-23a3-3923-ba49-151e02483d2f | -6.51324 | -46.64391 | 2026-10-06 04:40:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a470effc-cf53-3481-8b7b-8dc8ee7196c8 | -11.36146 | -46.67946 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3bb3460-e70f-3c5e-bfdb-3344c6f516c5 | -11.36204 | -46.67554 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8a3d962-a38e-3d6b-b2eb-cce0b4e5afd5 | -11.27836 | -45.50689 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 37f21a30-9beb-31ef-80b3-e28920ae323f | -8.0515 | -45.61868 | 2026-10-06 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f75e205c-3e0a-349f-9b5c-e001af0e4b33 | -8.00915 | -46.45866 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 756443f4-df9e-30f0-98b9-b6bf7482b6a4 | -11.83092 | -43.54509 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ea6cac-7a08-3468-a357-b3b39a45d218 | -7.47789 | -42.81345 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f004b135-d4eb-3d8b-be78-4458766bbbaf | -7.46729 | -42.99761 | 2026-10-06 04:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a11bd2af-16a0-3c51-b26d-3fc6be987b32 | -9.81411 | -44.79337 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef95e9a-fb37-38d0-a572-af5c8f28b699 | -5.82708 | -45.0108 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70a3cf01-a9cd-3b21-bc92-635a6420aec1 | -6.00035 | -53.51714 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f438d46-b41a-33fd-839c-f00b7ddb2c45 | -11.36785 | -46.66044 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c066ca8-37cb-3826-9a53-402f11b3922b | -10.50002 | -44.41529 | 2026-10-06 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c879e369-b720-3ae4-8130-b47fe05c6107 | -8.05132 | -45.61792 | 2026-10-06 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2abb33e6-fb98-3682-89fd-a696574179a7 | -10.96408 | -45.41098 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a20b131-5e66-3c2c-b542-fb99620cfe4a | -5.99552 | -53.5204 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7087b25c-61b1-34ec-8a51-5d04e8d61b70 | -6.365 | -42.5481 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e10ef4f3-c626-3493-9767-b4c1b9852e8b | -11.69056 | -43.67981 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9501fb8-0a86-3725-b471-745619e828f6 | -11.26228 | -45.51353 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 75c9e51b-67a7-3efa-887c-f5ad05b45a3d | -11.23652 | -45.26328 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c24c7b91-42cc-35db-a7c5-d3986c9ed5fd | -3.55395 | -59.48943 | 2026-10-06 04:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d5a2124-9fe0-3bf6-82af-694cb892d9ff | -6.60689 | -41.58231 | 2026-10-06 04:40:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a215928d-88ae-3c18-ba40-53ae8b024732 | -11.65096 | -43.65943 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21c7870d-40ae-36d8-9325-fb0abba6bfda | -5.81599 | -53.84134 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be560c61-bae8-3359-9182-c66d0c555c04 | -10.54509 | -49.49121 | 2026-10-06 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eeb34b5c-adfc-3fab-9395-1bfb3d43f29e | -5.68341 | -53.49246 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a228d8c6-8e39-3100-89e1-ddb4100406e1 | -6.84914 | -41.80414 | 2026-10-06 04:40:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45fc82a0-faad-3628-bbc9-6a0dab851991 | -7.82837 | -45.30063 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33cce53f-e1da-3737-8b58-067a4fac0b00 | -6.34575 | -42.54963 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ecd2cd11-fc07-3501-8ce8-0a2709f7929b | -11.27597 | -45.49744 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7ba6526d-9406-3901-b4d4-4f0f8d54e73e | -7.82863 | -45.56282 | 2026-10-06 04:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5545318a-2a12-3499-93bc-d5590be938db | -6.91951 | -44.55979 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ce73230-638f-3fc2-a66f-acfa50cf882c | -9.74433 | -48.17517 | 2026-10-06 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bb0d62d-9684-366d-a24a-fd1a97276081 | -7.41089 | -46.79219 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc73efcf-8802-358e-9606-dc2c8c89389a | -11.69218 | -43.67922 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0786c40c-766a-377a-9c82-4978c7932e19 | -3.70631 | -58.93925 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b7aa22b-8b63-3e4a-8feb-a497c8c219d1 | -8.52453 | -48.90889 | 2026-10-06 04:40:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 854ad526-2b78-3665-9469-0564b8db9c7a | -11.36089 | -46.68336 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 626cdc57-80bc-3b33-bad2-b70d44a484a7 | -11.68548 | -43.65574 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7abd868a-4746-3cdf-81eb-b315a1f57c82 | -11.28684 | -45.52631 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 684152b4-3f08-361e-b879-71ec67a11f34 | -6.37437 | -42.542 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eef916a5-f7aa-3b18-b7b2-312de952696c | -9.92007 | -48.13853 | 2026-10-06 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7e0d40-8997-30bd-ae4f-4bc8da8c0a5b | -9.76718 | -44.79805 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc1f7596-9e29-36f8-ad18-beec375e5616 | -8.7049 | -45.21109 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7eb277-fb04-3abe-8fae-55378f3ca1fc | -6.21334 | -57.77723 | 2026-10-06 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84074757-1337-313e-a07e-38a3fa5aa250 | -4.28173 | -55.76594 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd0de61f-9f89-3e93-8e70-dcda6ed46a7c | -11.28011 | -45.52076 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eaadecc1-c632-3dbe-99c7-9c9ca81d3c0c | -6.35723 | -42.54316 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5340c8e6-5bda-36d0-8451-01923f483939 | -11.26792 | -45.5008 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| eb19b687-0e32-3ac7-9ec2-aa089c462bc4 | -11.27576 | -45.52464 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| be0b7498-732d-3032-8a0a-3164cf1ff323 | -6.21397 | -57.77366 | 2026-10-06 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73988e63-5366-32f6-9d44-cde9f8c41c7b | -6.2298 | -47.00393 | 2026-10-06 04:40:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50995332-a531-30c9-8035-4a10406bb7c0 | -8.70189 | -45.2063 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54363a14-6d03-3797-ab71-4a78ec5f067d | -14.05043 | -44.29085 | 2026-10-06 04:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba97e743-7220-3dfd-9bdd-73581f890f58 | -14.80454 | -42.00558 | 2026-10-06 04:42:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1eee8f9-fe56-3532-8b01-e907ab34898d | -11.99057 | -60.47888 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fce48a3e-9405-3518-b732-8966ca48ca5a | -14.80383 | -42.01113 | 2026-10-06 04:42:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a1e45a71-f9d0-3c17-8507-59e1d963b11b | -16.02101 | -45.13272 | 2026-10-06 04:42:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b5ea1e9-8e74-3a84-b252-89298fa7fac9 | -11.98767 | -60.4794 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81a6ad48-3b09-3642-9384-ad7647c69448 | -13.87655 | -43.79443 | 2026-10-06 04:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc91c00b-e884-3867-a16d-5c68f763d5f7 | -16.0395 | -45.11687 | 2026-10-06 04:42:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5beac7f7-b222-3f44-996b-2aba912ace84 | -13.49972 | -61.14159 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ef12f4-a746-3e48-950d-f7626d032692 | -12.60805 | -60.90346 | 2026-10-06 04:42:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8f72b4b-d013-3c9d-877c-c4fcad4a08c4 | -18.53515 | -41.30284 | 2026-10-06 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7680c225-263f-3fd0-a096-492118f82313 | -11.98859 | -60.47477 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35daeab4-77dd-36c4-898b-3cb36da3e2ee | -14.78342 | -44.65654 | 2026-10-06 04:42:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e67122c-1c79-359e-842c-1eb09a1ed722 | -17.71342 | -42.27959 | 2026-10-06 04:42:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8af6a693-01d7-3a95-be00-b7c7f2a4651b | -12.12918 | -63.16374 | 2026-10-06 04:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README51.md)
