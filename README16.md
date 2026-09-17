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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44bcdeb3-0991-3fb8-927e-393855379b88 | -9.6093 | -45.36325 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ad87755-bc84-3464-a5af-bec464cc2a44 | -11.27922 | -43.47778 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 850c250e-eda0-392a-bce1-233a8ada7ff1 | -8.26024 | -42.17577 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5ef3342-059a-35cf-a5c0-ae94b624ee24 | -8.56414 | -44.54783 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 615e6e99-94b6-32ca-8bfb-1f37511d883d | -9.94754 | -45.30231 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba49f4b8-e1af-3142-a6aa-3ff40414d4ba | -10.04749 | -45.56336 | 2026-09-17 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 201a45b7-a9ef-33db-9c87-54ea2d414af7 | -11.16783 | -42.79162 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 669f45da-9ab6-3af3-96bf-929c402f6542 | -11.35753 | -44.02539 | 2026-09-17 03:36:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e89edf9-97d3-3c10-9e94-e987afc62432 | -8.3928 | -42.20606 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d141a733-0225-318f-8a0b-5b118f0dff12 | -7.65052 | -44.32683 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b41ca665-fdf4-3adb-9e93-5408bbec7c8e | -7.08771 | -41.84562 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d856259f-32c1-30b5-b565-89fa8249f947 | -7.72223 | -42.50274 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5794ba49-2038-394c-8aed-643d4f04c7ba | -6.6802 | -43.65187 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6fa9eb-73f5-39b1-be00-07a1c6d38ec5 | -7.81228 | -44.86512 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 870c01a1-4b53-3808-bd05-9845b9a50d65 | -8.47514 | -44.55711 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9a430e1-8570-3136-9267-0e1c55f6047a | -8.55833 | -44.54051 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73ebb1f1-60f8-3200-88cf-29f7c7270679 | -9.96011 | -45.32727 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 97466c18-1599-3ffe-b04f-5e2c6213083c | -8.56314 | -44.47927 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 254ae520-5289-3345-9517-9c070952c56a | -9.49123 | -45.42739 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3565674f-7b0a-33ac-b5b4-d1d216c33a97 | -11.27395 | -43.4714 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03accfe7-4a16-3b36-b680-aebf375ff8d3 | -11.26868 | -43.46506 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b810069-6e0d-35bf-aa73-553696954324 | -8.46835 | -44.55471 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 773a1a39-e033-384e-a661-2d8663815bb8 | -8.94797 | -44.39795 | 2026-09-17 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1a81fe5a-3b04-3628-a174-f25a44ca778a | -7.13303 | -42.17376 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5eb7c650-f576-39b1-92c2-ef672c8a7420 | -8.60969 | -44.49163 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e52fd571-ee3b-319d-8399-b009b4ae8c0e | -11.27295 | -43.47647 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b8c8d2-5da4-3cc7-b9ad-975d283ce5f6 | -7.36756 | -38.97932 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3f259bb-f877-3a23-baba-d32cb02afe56 | -7.12249 | -42.16146 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4ede174-71de-35a8-90f5-fbd66a2637d5 | -7.0263 | -42.06938 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44d9910e-9aa6-3d42-bea8-f62ece03fd89 | -8.85504 | -44.89355 | 2026-09-17 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd1ff8f6-2422-3a6a-8bf1-fd89cda50be5 | -9.60541 | -45.34538 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d62eb5f-139d-3ad5-9339-5b3c66d278ab | -7.12891 | -42.17337 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49d34dc7-5619-3660-aef3-33fda4db53a2 | -7.12362 | -42.16714 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24c664a3-d914-3e95-9268-7375fd2fd26e | -10.54264 | -44.84983 | 2026-09-17 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e544df49-8c56-34c2-9723-97a70d0a00e5 | -7.43941 | -35.24736 | 2026-09-17 03:36:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f2f4fd99-ff1e-3fb2-9ee2-8964bdf27709 | -8.57885 | -44.57276 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed3e6527-d72f-3e35-afa9-01ddac2bf418 | -7.08759 | -41.8494 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5fe2766a-5462-3371-8777-4304fb6c3bd2 | -9.62221 | -45.37346 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e4a89695-374a-343e-a31d-6a5b27d68268 | -8.58028 | -44.57656 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd7d9281-c1ba-3e4b-849e-315dc4961457 | -8.4738 | -44.56377 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9110b04-03c2-3f06-9637-1b83090a22f7 | -7.96768 | -44.84412 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fae333fc-0acc-3ecb-9cbd-4d099d750c04 | -11.26557 | -43.46015 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f90919b-ef1a-30f6-b2e3-02c5b11649f1 | -11.16181 | -42.79035 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 796313d0-66e4-3651-958b-ccbf0d27a89e | -9.62526 | -45.3648 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ca4dc29d-f417-3403-bb44-d91c2530ec83 | -10.54743 | -44.85606 | 2026-09-17 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb59c8d8-c6fc-3e44-8bca-d52c97019bca | -7.72316 | -42.49767 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c0dd1e32-e824-30e6-ad74-ef5c1271fbd3 | -8.47071 | -44.55722 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f7f051d-5330-346d-a4fa-bb2484e6fe7b | -7.08684 | -41.85026 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a59ca054-8e46-35d9-93ce-14c81d63fec6 | -9.96466 | -45.32792 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93485d3f-2af6-3797-9eba-bd4ac09fb09f | -9.46352 | -45.44676 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 319a6665-bfe5-3d13-bee8-098f28291d86 | -7.12273 | -42.172 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69dbda86-e6d1-3918-b420-a9d7846c7d58 | -11.28858 | -43.47536 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 772cb0f2-83ab-3f8e-9723-c352a34bbd22 | -7.09474 | -41.84178 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 88a7519a-f8c0-3f8c-b5f8-19ff65743304 | -7.33755 | -38.14028 | 2026-09-17 03:36:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1092899b-d3e0-3eb2-b6e9-0051ccb0bb92 | -6.03974 | -44.0351 | 2026-09-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7a78487e-17ef-3952-bce5-1d6c2bca1fe9 | -7.36737 | -44.48502 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b72d91ee-0e8d-3df5-9c7d-0cb1553e900c | -7.81345 | -44.85223 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c1affd-06e3-3123-946b-b42f5b14b050 | -9.47099 | -45.44699 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a8eba52-be14-35b2-9eab-0628ae2b1b6e | -9.47047 | -45.45492 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 10886dc5-f124-31d6-a88d-b5d71a372bbf | -7.09192 | -42.09526 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4259a333-cd7c-38c6-96c2-197bff13a222 | -7.33352 | -38.13826 | 2026-09-17 03:36:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d683b7f-ad6e-32d3-a1c3-7e4f30247c28 | -9.46477 | -45.4461 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2555354f-c811-345a-ad43-d7f1d4cfff00 | -7.36502 | -44.47719 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a695f11-be82-3073-90d5-3e3fe544505b | -8.39887 | -42.20742 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2f5f77d0-0689-35bb-b3f2-3720dcdedb71 | -7.03882 | -42.07092 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 05c48b10-34e9-3176-a6d6-6ccd0a142825 | -7.04023 | -42.07545 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5cdcc67e-0695-3144-8b93-fafcddbb3841 | -7.36019 | -44.48411 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662104bd-29b2-3909-84f6-92983c263ed9 | -7.02345 | -44.63193 | 2026-09-17 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf3c866-2821-3f5d-a8f8-d57382806851 | -7.33829 | -38.13912 | 2026-09-17 03:36:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b388f62c-89bc-3a5e-a4d8-20fc9ca30429 | -9.61963 | -45.34897 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d3e1e43d-0f86-36b9-9f11-f668aa5353c3 | -8.94188 | -44.39785 | 2026-09-17 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7817b415-2294-3552-83f2-0812f4d22a35 | -8.56295 | -44.55386 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5cc234c-6e7b-35f4-929e-de4525e2119c | -7.02956 | -42.06374 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8289681e-c1b1-3c42-ae57-5f439c45273b | -7.10111 | -43.11442 | 2026-09-17 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae8cb0c3-7a81-3e14-9a44-3d24759d8116 | -8.57744 | -44.57972 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b590bac-3fc3-306b-bc76-866e3b36328e | -8.256 | -42.16472 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13db9b99-5e35-32c5-b5de-a4ee167746a5 | -9.95906 | -45.31884 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c80c1c7f-df9f-3c65-94f4-298219816406 | -6.93177 | -41.70254 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| aba87b67-fdd8-300b-bcd5-58fc917a6f4a | -7.35785 | -44.47628 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eedd18d-4e82-3417-9320-0ff53e5d1069 | -8.55642 | -44.4767 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86ee383d-afa1-3fd9-86d1-14152b0e697b | -7.08239 | -41.84333 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2a4a92aa-a4fd-36df-9408-0f8db7fffea3 | -6.93259 | -41.69809 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cc90ce79-aa5a-3513-bc02-1f7f52cc45f7 | -7.14204 | -42.16013 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3cfbdfd3-2c73-3946-8920-8c4243b5bf83 | -8.86088 | -44.90112 | 2026-09-17 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52f1c45c-28c7-313f-b274-c39ed348cac2 | -7.94032 | -44.83197 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e751f355-96fc-3d88-88f5-9bcc8b07f042 | -8.60841 | -44.49801 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8ec464fa-4ba6-34e1-b66c-5f0a0fda245b | -7.03399 | -42.07452 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 01a33cfe-403a-370c-8d43-2bcb0e3a8693 | -9.96616 | -45.32044 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4963aee0-4465-390c-811c-ba5fc8d546ce | -9.95038 | -45.30252 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c475c8-3c97-3625-86d7-1badb0ffb0bd | -9.61662 | -45.364 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f83d6989-c431-304a-a4ac-2e73ca8a501d | -7.14111 | -42.16507 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52e47e52-416e-34d8-97c2-937b23c1fa1a | -7.36149 | -44.47723 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1e21c8a-b2f0-3cb8-9a83-66e480447854 | -9.4631 | -45.45412 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 47aa5f0a-295a-32fc-a709-def1e59cba39 | -9.95209 | -45.29423 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af73a8dc-7e5e-3de6-a79a-6d6be9cfc7ce | -8.3985 | -42.20999 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 82388403-d9a2-3a31-808a-4d72ad8841a5 | -8.46937 | -44.56407 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b03b275b-4a79-37ec-a2b9-3a572cc6e413 | -7.37821 | -38.97789 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9d2e8202-55b7-3d04-9b8d-ba319d31456e | -9.48993 | -45.42762 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d2173c1f-c4e4-34f9-a54a-694ad00b28c7 | -7.36864 | -44.47824 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dc633b4-6334-324b-a678-957531c399f2 | -5.29417 | -43.63802 | 2026-09-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README17.md)
