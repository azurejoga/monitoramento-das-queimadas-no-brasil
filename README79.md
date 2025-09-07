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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9396584b-dda4-3fcf-ae64-7f9570d37d73 | -11.2014 | -55.06039 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ec776c-894d-3afa-ae91-e9a2d542bfba | -12.412 | -63.89683 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26bb9c53-0b8f-3bcc-a461-52d33d91f971 | -10.58075 | -61.2325 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 449ff581-40c4-3040-8bc8-dca3e5e02d93 | -11.20571 | -55.01496 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b0cd427-1a91-3f01-92df-246fbee48259 | -9.43518 | -62.36734 | 2025-09-07 05:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a94e66af-ba63-3176-ad5f-3b0ae7c37c08 | -13.89577 | -53.99636 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 007f5f4e-bb95-3d6b-b769-156360637290 | -12.41761 | -63.90515 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3b8820-a108-3a2f-a6b0-b3d1c53e5500 | -12.80749 | -52.90952 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f503ebed-7933-3855-a016-ee551d25683b | -12.81854 | -56.5242 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e11135-47b1-3e19-85bb-21dc182a1bcf | -13.93699 | -54.01705 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 480b7e1b-f060-311e-8622-b1b9f940a44a | -12.94882 | -54.79158 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e12d9bf-c882-390a-b193-3cee5da2ba69 | -10.88014 | -55.72285 | 2025-09-07 05:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a11495c4-8425-3d18-9eb7-4580209a2c7d | -12.92859 | -54.76632 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bccb2e6b-77f0-388b-acdb-4b0689f5b392 | -13.94215 | -54.02634 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec6ae8cf-eb97-3a85-a348-5f8e29e270f9 | -12.19532 | -53.90593 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898f8421-60e7-3b27-a30b-261f821e04e9 | -11.22148 | -55.0245 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5037467-47b3-3f76-8ec7-3310f874c9db | -10.8383 | -55.09864 | 2025-09-07 05:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53790dbe-e8dc-358b-9433-178eda38dc9b | -12.95364 | -54.80036 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c799e16-9eb8-3b5d-afce-dc0feb0bf494 | -10.88581 | -55.72052 | 2025-09-07 05:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e55379b2-a616-3873-9494-4c4da47a27d2 | -13.89633 | -53.99138 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9aad7170-aefc-351a-b4f3-51c7c11f9929 | -12.63273 | -56.98066 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b2e8f17-d50a-38ab-bfdc-58e9044cf31d | -11.22239 | -55.01712 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76bbf40c-ce02-3ff6-b509-2a220441be00 | -9.35389 | -65.4268 | 2025-09-07 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25be73b3-939f-3eca-a880-8c6a77cfe41a | -15.70235 | -53.56031 | 2025-09-07 05:40:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb24b584-2819-3936-b5f5-bbd0f3de9f4e | -10.17093 | -61.13854 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4883465d-f397-3986-9480-01e9d97a6ed0 | -16.29109 | -58.11837 | 2025-09-07 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fcea3e70-f176-3b43-a779-854e2fe7804d | -12.93292 | -54.77721 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa313ff9-5e1c-3718-b669-92cc380717f2 | -9.4323 | -62.36303 | 2025-09-07 05:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 317aa9db-4d84-39d3-a897-d90287c41aec | -13.77152 | -52.77765 | 2025-09-07 05:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c07c035e-a85f-345d-9e7e-a7774bd51284 | -10.16668 | -61.14199 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31fd8521-5f75-37fe-b091-3c32ec2c931b | -9.35446 | -65.42322 | 2025-09-07 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c7646d-67d3-3f74-aaf7-14e2010099db | -11.21591 | -55.02384 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14eaeabb-3d01-3cb4-bf94-09feb0971a68 | -12.35771 | -63.63855 | 2025-09-07 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cd644b4-497d-37e6-bb41-0c3c180b1436 | -13.90242 | -53.99256 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bdd5666-998d-3b63-9f77-dca014149053 | -12.81366 | -52.91597 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df1dc081-d11d-32b3-beb1-230be34b70e2 | -11.22843 | -55.01393 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d271d817-baec-3228-a472-7ebc18121b90 | -12.95024 | -54.77945 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3dd4e45-5e80-323f-8342-189e8f1c4fdd | -11.8306 | -62.92849 | 2025-09-07 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 239aa2f5-1a87-31bf-90ef-1083f5a375bd | -11.71838 | -55.29629 | 2025-09-07 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98993ada-ee8e-3bfb-8e6f-bb83e07e34d7 | -11.05017 | -54.17365 | 2025-09-07 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 189ed29e-d34a-373f-aa43-e8efb1c482cf | -11.20032 | -55.05899 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48cf1237-824d-365b-8fc2-954b3f82ca9d | -10.76921 | -59.8497 | 2025-09-07 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2574db8e-fd6c-3b03-ab23-d94d0438a2d6 | -13.92233 | -53.98159 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9178c43f-f09a-3ddd-abee-a586a6d88a0c | -10.46687 | -53.61528 | 2025-09-07 05:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbd60588-d1f7-3a9f-981f-e0205988769c | -13.90793 | -53.99895 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0306a9c-33eb-3520-b5e1-f38d2577c66a | -10.87447 | -55.72512 | 2025-09-07 05:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e05b8365-d71b-3c36-b9d0-71aa35e99e46 | -12.94493 | -54.77471 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 0e35b658-9d31-32c4-b921-3ee3251d0c7d | -10.42346 | -60.74992 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f5c206-ec0c-32f3-8674-e8ac7375a009 | -11.48472 | -55.55844 | 2025-09-07 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 112ae615-3183-3cde-b6dc-3ee066e2d7bc | -14.42216 | -60.18919 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 081443e3-021e-39a8-8dfb-64280dd6a154 | -11.32026 | -55.22109 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efeeaac4-1654-3521-b6a2-f27fbe07e508 | -15.84805 | -52.27437 | 2025-09-07 05:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dde1243-f30b-3d3f-8a5b-865616ac0e74 | -15.69588 | -53.55991 | 2025-09-07 05:40:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8d2a117d-34e1-34d2-a326-c3924c9e1bb3 | -15.83417 | -52.27256 | 2025-09-07 05:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a1d75da-6158-343c-9ca2-542013585181 | -13.93589 | -54.0272 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b2f0975-8718-3486-af15-3507481dfd87 | -13.7709 | -52.78361 | 2025-09-07 05:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b34effbd-18aa-39ef-97ac-167bd11793c1 | -12.03047 | -63.36158 | 2025-09-07 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c55d457d-87b6-3385-85bc-a366e2123e6c | -11.17907 | -55.04855 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3962fa0e-08e6-3beb-91a3-e43a83f5bfea | -12.84294 | -62.03394 | 2025-09-07 05:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08394c6-1309-3a44-88c3-b8a2e2615b29 | -12.62206 | -56.98501 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fae3f4d-bc46-3e37-9a77-f7319c50b409 | -11.17862 | -55.05222 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbbf018f-1a1a-347b-a788-a76c31051f33 | -12.94588 | -54.76652 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| aeb59371-bd89-3fe5-89e9-b37fe51327a4 | -12.84655 | -62.0345 | 2025-09-07 05:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c7163d0-8982-30d3-9ff7-8c3d275aa702 | -15.88353 | -52.19786 | 2025-09-07 05:40:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 16cab1b2-e97b-3dbf-9dd0-ed3bb09860ed | -11.63968 | -54.53898 | 2025-09-07 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4463e0-a837-3fe9-8341-9b7c6b7a0f10 | -12.19586 | -53.90125 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0c6b7d7-1e30-3038-9ee8-96e651ac6f53 | -10.46086 | -53.61437 | 2025-09-07 05:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8436f5ec-eb7a-343b-9053-f2652f8d2abe | -12.72016 | -56.56059 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c91f853b-4841-3e69-b969-efd9190b2b9d | -12.93962 | -54.7699 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| bb41e671-e674-3f70-b17c-16ceea05b2cf | -12.94789 | -54.79954 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6363838b-1bd8-3ec2-995e-da9e2fecc15b | -11.20617 | -55.01125 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 511ba61c-9539-315a-add9-2f4c17f5f3bc | -13.94252 | -54.02334 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5391ea55-8c42-3894-81ef-66daec535cc5 | -12.42266 | -63.89481 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4c9c5cc-2966-3bb7-96b7-36dec0a7bb77 | -12.9565 | -54.77595 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 859c1aed-e41e-38a3-a115-dc90b4bd7597 | -14.42166 | -60.19291 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 457e6ad3-c21f-3702-b0ff-682d3cd84199 | -15.84105 | -52.2741 | 2025-09-07 05:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85f2ac52-2857-30d8-a02c-eb0c82c26fb7 | -11.82829 | -62.92035 | 2025-09-07 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f6bf177-ed27-3b44-8a98-236c6a38e992 | -11.20122 | -55.05163 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bf8a474-99e5-3030-a943-b740eaa5ccbe | -13.28308 | -58.46198 | 2025-09-07 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 437773ef-2d98-3a1a-abe3-3ba39d4e6752 | -11.1802 | -55.05007 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8811409e-f8d1-3743-99d3-905d108b179c | -12.41537 | -63.89736 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 270d8fd2-84ad-380c-a6c4-cd4aab48f1de | -16.29044 | -58.12376 | 2025-09-07 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c9299c4a-a98c-31ac-8c14-0bea6748b0df | -12.81425 | -52.91051 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f154e6d2-c120-35a9-8f90-53e490cd89dd | -12.95553 | -54.78425 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7800b773-f5bf-3ca4-9c14-0e1b944c1917 | -10.16555 | -61.12397 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b224934b-2dae-3c88-95e8-6c09b0d4d106 | -13.90185 | -53.99768 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b5410b8b-3a41-37d8-8c0a-9a82c0f5017b | -11.16432 | -59.15783 | 2025-09-07 05:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a503b0cb-512d-3ffc-a7ce-1ebde34c7f75 | -12.81893 | -56.5212 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb6c3744-7303-31e5-b308-6f46de6b4414 | -16.33167 | -52.94955 | 2025-09-07 05:40:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2148b781-0c0b-3788-8803-2d09978bf8b6 | -12.93915 | -54.77399 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 676c242d-83bd-371f-a4c5-e9f2d97313a4 | -11.17974 | -55.05371 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e046010-9878-3990-8287-ef67d477783a | -12.35489 | -63.63435 | 2025-09-07 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 324aab07-7b90-32cd-b73d-67f6fa666089 | -10.57761 | -61.25418 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d36f6df0-021e-3a05-be60-eca5ef67beee | -15.57118 | -52.90559 | 2025-09-07 05:40:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c23485a-4c3e-391d-9064-87f0aba927b8 | -13.91298 | -54.00938 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a3f2dc7-2653-3adb-bb9d-fe837f0ccf8f | -12.61711 | -56.98428 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bda7bcb-0086-3e15-8df4-769f62dbd926 | -11.21682 | -55.01647 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1565ac-e6f2-3d6f-af1c-6a9cdf66840e | -12.93339 | -54.77314 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f283003b-784e-3fc2-a9c2-6c5f16c0dea8 | -12.9401 | -54.76576 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1779a244-600b-3dd8-9d9b-958805a14174 | -11.21126 | -55.01578 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README80.md)
