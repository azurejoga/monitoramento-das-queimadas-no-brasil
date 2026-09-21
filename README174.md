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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4965dfec-b44f-377f-a8de-a62bc8dd3ee0 | -6.84142 | -43.77329 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d91d2ae-9cea-34d1-99b8-287e7c97052a | -5.74515 | -43.70002 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 89a718a5-9ff3-3ffd-a3ae-c32c81d67e86 | -7.27792 | -45.55994 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac9dc3b7-7810-3b38-9599-80fc86b0f843 | -5.55547 | -45.69477 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 336142d1-e22a-3196-9b98-bed3f5ebeb95 | -6.07619 | -38.29716 | 2026-09-21 16:03:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d4573da5-0a75-34f9-8f92-fb797b0ff66e | -6.92228 | -42.95292 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 9c356444-1439-31e9-973d-247ed45771a9 | -5.29092 | -47.87606 | 2026-09-21 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0ae0e89-80c3-32db-822f-22b362391ff7 | -3.17866 | -42.83921 | 2026-09-21 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 99b0f70a-6651-3be0-b98a-4775419ac0b5 | -6.22307 | -45.92212 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b5a2c860-2881-363b-bc90-0bca69147d91 | -8.43996 | -45.82457 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 273a2a31-eca0-3b5a-8448-dbb1c1ceea19 | -6.0555 | -45.32026 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e08c7879-206a-3403-84e5-cc08eda1b927 | -6.29036 | -47.64675 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d2770aa5-4272-3d45-b542-416e8e8acd2f | -6.49684 | -45.87876 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 3abe8d6a-0927-3ff3-8c92-398ef255b072 | -3.57418 | -40.31894 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1d3cea10-66d5-3b24-8ea5-e8b23ee2af60 | -3.33612 | -42.54036 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dfbe10ac-ca2d-372b-99e2-90cec458a4d3 | -3.59941 | -40.34849 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8b6b496a-8b85-3715-8099-6932908e7aea | -5.65434 | -43.42165 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5295d277-0500-3bfb-9672-bb4329010bf6 | -5.34375 | -45.96373 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0257a7e6-267f-321d-b9e7-05f5826bd629 | -6.90616 | -42.92648 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 7f2ca241-6e44-34bb-be7d-5728cafcb746 | -8.38547 | -47.27895 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 49a70aa3-fa18-3fe6-bb92-45f3de1de33d | -8.39097 | -46.52047 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e6ac7053-b87b-3e30-9a87-d817f2a6c68d | -6.75354 | -43.73285 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1525f2b-dd12-3185-a8bb-e86fda40f9f0 | -4.11152 | -46.40157 | 2026-09-21 16:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 793f6e47-ef7b-3a3f-8210-b959cdc58c64 | -6.24273 | -41.65255 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 0add986d-9e48-3d79-8937-6c0d8da42aca | -2.46944 | -49.82066 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ba91493-4d57-35a5-954d-af7aaa842065 | -4.11467 | -46.40377 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| cb647eeb-1240-3c46-9bbd-bdb0ab496cf1 | -6.18951 | -47.49244 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 80f3d36f-ce22-3ee0-ba7a-8f9efc2bd2d3 | -8.34271 | -47.54466 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 90eb3f3d-27ef-356b-b65c-fe94cd6a14a0 | -7.88209 | -44.823 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7a607f87-6d88-3034-9db8-3b81072de9f6 | -4.11872 | -46.3972 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f2c3db62-c9e1-30a0-b26d-3a8378422b4f | -6.92957 | -38.72805 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 602ec5df-cfb0-3f7e-8a25-9363e7788e87 | -8.38848 | -47.176 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7d4eab6-fef3-3219-9462-677b8dc30881 | -5.99185 | -45.06966 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e4de427-276a-3302-8517-d8bbc3078a36 | -5.77374 | -47.36917 | 2026-09-21 16:03:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7d2bbff-c462-3f73-8678-c1b8f913c8bb | -6.91786 | -38.74052 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bd889cdb-4508-3469-98e6-c002cea30871 | -8.44032 | -45.82735 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 805d49d5-1ad8-3e61-b04d-070ae466b7ec | -6.42411 | -43.30594 | 2026-09-21 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd41fde6-11a2-3cb5-84de-0375d228dcc3 | -7.1208 | -43.08866 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1701fce5-4559-30fa-9f65-cd529a53a91b | -6.22772 | -45.43691 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 06b19d30-1ccc-3e61-89b8-ae088d945a31 | -8.43907 | -45.82067 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5bd5a10a-b1d8-3f24-a810-a54809211ec3 | -8.49171 | -47.02381 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f09a451c-73ad-3c8f-afb5-4f7100ceeff6 | -8.38965 | -47.17763 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 73ab9ee7-7bbf-3bcd-85db-06c0daeac539 | -6.74307 | -46.61849 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3a2f540d-3956-3b97-8346-a0ede318d655 | -4.59096 | -40.57767 | 2026-09-21 16:03:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 247b8ff2-1514-3ac2-a75e-bc15ffaf1b9d | -3.28284 | -40.64346 | 2026-09-21 16:03:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c42e4927-02ef-3f92-8ad9-a7c1137c1ef6 | -8.34218 | -47.54073 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b1f5b1bf-3ae0-32ad-87a3-39eb2fd8be73 | -8.48189 | -47.02031 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e481243e-fbf8-3e9c-b81c-42ac4521b194 | -6.39403 | -45.19452 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 71fbea9e-6649-3159-99eb-87d07fd70298 | -3.64266 | -40.58902 | 2026-09-21 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 367f7202-0026-30cd-b71c-2ee828478b75 | -3.76468 | -40.20875 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 76c14b3e-7ad5-3887-a075-ffc866d04f9c | -6.23967 | -41.65741 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 1db09a07-aaca-3778-a642-f9de4dbb76b5 | -3.25468 | -42.95703 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a04e5c67-55d7-3438-bb14-3bda46b35e3d | -7.75422 | -46.72477 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 5b097779-7e76-3cda-8b8a-f45044f92b8f | -7.53489 | -48.69573 | 2026-09-21 16:03:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ffccc562-4c98-30e4-bfa4-733b47684946 | -6.042 | -44.85685 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 303789eb-43af-3b38-924c-e0d815abbd46 | -5.53761 | -45.67123 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 834b2eb0-a05f-3b30-901b-bebe34d564e1 | -6.80327 | -47.90232 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9cd039c-1f32-38e0-9aa3-62b40e85cdff | -4.4636 | -38.29059 | 2026-09-21 16:03:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 0307c722-d3b0-37f5-9267-0333a13321e7 | -6.5579 | -45.55024 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| dfaf3b6f-5876-3948-b877-37ff5aca8959 | -5.4067 | -42.9541 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8eff7def-e822-35b1-bbb1-f933946c3633 | -6.83743 | -45.557 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 84afd6bb-f3b1-38eb-a1b0-2bdb73eddbbd | -7.05333 | -49.91045 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3db3b511-e852-3bc7-8fe5-cf2a7f7afc56 | -7.82857 | -45.26451 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 84976494-bd96-305f-9ef2-2ff2debe5b36 | -8.39576 | -46.51638 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 78c9eee2-b0a5-3b4b-93b6-dd47690ac109 | -1.45268 | -49.74921 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c345514e-17a3-31f6-a2f8-9a63d1a7d126 | -5.58041 | -45.53205 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6eed3170-7f13-34e6-ba7c-b94bcb5489fb | -6.6854 | -44.06672 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 817dd4ef-5638-3e6f-9537-e8b17d3673db | -6.3707 | -44.89584 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70c7c327-94e7-33c1-9f68-5507a9d3a2ed | -6.99111 | -44.70688 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0fd934d0-c619-3e5f-9495-096f6b96624d | -6.25011 | -41.65152 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 305.0 |
| a1ac1213-5dcb-3688-b0b5-140d9eb94003 | -7.11468 | -43.07473 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6f4095bf-ca65-3a13-8a44-8ec829a7c489 | -5.55147 | -45.70077 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 1adfe5fc-1649-313d-b4db-012ae233c951 | -7.73267 | -43.88664 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 698f5c7a-7749-381f-9976-2d399833047d | -7.97807 | -44.07495 | 2026-09-21 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b6e24583-f817-3517-828c-c77dcf1bc2cc | -6.55699 | -35.60173 | 2026-09-21 16:03:00 | NOAA-21 | DONA INÊS | PARAÍBA | Brasil | 2505709 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7cd6ae2d-7856-3346-9140-726752ae4522 | -6.92677 | -38.73204 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 91643cbb-4553-35bf-9d01-0cfb35654490 | -4.1384 | -40.62202 | 2026-09-21 16:03:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6ffad90c-a502-3c45-89c3-f13041cbd9f7 | -7.42329 | -42.11537 | 2026-09-21 16:03:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| f5fa93fe-27c5-36f0-bfb8-c7986b118951 | -7.18139 | -39.36103 | 2026-09-21 16:03:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 0f9307f9-a28f-329b-a553-0472d4c933f4 | -4.51175 | -44.96026 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 64aff02c-264b-3cd5-8d00-4a2091d720aa | -7.16847 | -43.01611 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dd0994b5-a7ff-30ee-a47d-6af3fddf7df3 | -8.42948 | -45.82239 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16d794d0-0df8-3eef-90dd-af86abde7381 | -4.6878 | -40.14984 | 2026-09-21 16:03:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fa2a373e-decc-3b9b-9a86-8f6d62cef920 | -3.32248 | -42.55149 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0ebbed23-cc3a-3b09-924b-ec96203426f3 | -7.72326 | -43.89595 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4031b71b-35f7-3d20-aa6d-a1f58bede665 | -5.02083 | -42.97593 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a9dca9fd-74aa-3c64-8cfd-50c61a39275a | -6.49408 | -43.48186 | 2026-09-21 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42c9b03e-19b4-33ea-b3a0-6ba57d068cc0 | -6.97394 | -42.58883 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| c5f0cf65-c387-33c7-99e1-d6d275461183 | -3.08936 | -43.62014 | 2026-09-21 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 548edb93-b8aa-35aa-8193-b267900fb021 | -6.83678 | -43.49319 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9865046b-52f7-3972-b9b5-6032234cd7e4 | -6.28077 | -47.65835 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9091635d-9d7a-3b23-9b3f-8455f4fad293 | -6.25812 | -41.65487 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 655f1f1f-3ee2-33b6-813f-d1437e4c7b43 | -8.30808 | -45.98425 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 81c7ee02-d4dd-3aed-9a14-d1a6135ecac9 | -5.29916 | -45.75404 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2aa8ab5c-1f2d-33e8-8ce4-cb9eea2b1bb1 | -5.61255 | -43.39073 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b9ea4427-5502-39e1-93ac-1c162fa539a6 | -6.66291 | -50.88646 | 2026-09-21 16:03:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b1a18d90-a9e8-3cf1-b68b-80f5075a618d | -1.39186 | -48.9502 | 2026-09-21 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9ea2cdb-e42d-33e0-a7e6-88784ae79d13 | -3.20984 | -42.47029 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cf679c86-8de3-32f0-8f81-f6e1d702ad27 | -6.5724 | -45.5513 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1e093303-0597-37a5-83b3-1cdf158e32f1 | -7.16989 | -37.71046 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 8.6 |


[Clique aqui para ver as próximas entradas](README175.md)
