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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a904c6fd-5ba5-3e87-b3df-00df0f8b4562 | -9.44076 | -59.20785 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 5b80ca90-5fa1-377e-bdd7-d57439eb1267 | -12.93538 | -54.78227 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5192474d-c1d1-3690-a783-6d2ebdd205cd | -11.88874 | -50.96264 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 315ed84a-a0e2-395f-ac7c-cd94ce4754f7 | -10.05534 | -59.36287 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d514dd7-b8d9-3431-960b-b72d11d27b52 | -6.22548 | -49.42372 | 2025-09-08 05:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 548e0b0a-f210-33ac-949c-3204fbef37fd | -10.46514 | -53.60565 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5754c4e-c022-3097-82d8-32a90d9bbf45 | -9.08207 | -46.97835 | 2025-09-08 05:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18bdac99-9900-3132-b3b9-6be50ca74832 | -11.03442 | -45.9512 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f3b195c3-6e77-37c5-90b1-c84443eb6315 | -11.02876 | -45.93702 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31b546ab-38e1-31a3-97a9-33ccb31a343f | -10.41607 | -60.80125 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40b3a62d-1a92-369d-b4bf-0167f9ce6ef7 | -6.82527 | -51.87801 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b61a596-3655-300d-aefc-54d236dd20f0 | -12.62861 | -56.96833 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f492d985-f9ec-3fd5-9435-7122a5862521 | -12.631 | -56.97761 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa9e3e8d-d958-3a92-b48e-6c32971cd06b | -10.14103 | -46.18843 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e034ca7-3a57-33c2-8c34-030c464475aa | -9.36814 | -65.93767 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d4e40f2-55da-3092-9216-320898ae9d96 | -10.57626 | -61.25739 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a14e9560-8b0d-3fd4-8e8c-097ebf228ce2 | -6.62369 | -53.34559 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0edd4b66-ab41-3635-8f49-e752313d9c42 | -11.86542 | -51.06538 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5cb9dae-f144-3db4-9025-ff5c6aa6d80f | -10.87322 | -55.72607 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4dfec5-74f1-3062-8135-3013a043d7a7 | -6.62856 | -62.83624 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a6c09d8-2324-3953-be4f-96d281296994 | -9.48359 | -55.9757 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a9f04a9-22a6-361e-b199-eb1da38e2be0 | -6.53487 | -49.50163 | 2025-09-08 05:21:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968bb99c-f933-3405-8dca-b1eff9eb1d19 | -12.61636 | -56.97538 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e17f928-c4e0-39e6-bd0b-e1d182972b62 | -12.63037 | -56.98197 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34f820d4-42f5-3708-b580-f02638496275 | -12.82135 | -52.88509 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62c2939c-7e96-3388-99b1-8c87ac79913e | -9.30031 | -66.61554 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 749b207c-22d3-3f7d-ae1f-a10c0b5952db | -13.81773 | -46.28693 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d9def53-e247-31c8-80a2-81c7c3dde41d | -12.94742 | -54.78797 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e30fb6-2000-383b-8b5f-0214490ec562 | -11.38974 | -50.34057 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c382ecdf-4f52-3f05-95ac-2417925c655a | -9.35087 | -64.26476 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0727c286-267f-3595-998c-aa7fe4b2f370 | -6.15509 | -53.68371 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a9eba1c-c132-37b8-b7bd-c2345c174c23 | -12.95482 | -54.76515 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 008898f2-561f-307a-b27a-dc5eb5e726bd | -11.22757 | -55.00845 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be96a91-53c8-35c7-9b6f-8fac9cea252c | -9.24489 | -57.07003 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 777f755e-06c8-3afc-bc34-e80cad37c3aa | -7.21826 | -46.19128 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28e0507-8cb7-357b-a471-b99832e3246d | -9.68581 | -63.16784 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 859715b3-5530-3828-94f6-a56ca491f2c3 | -11.89181 | -50.96175 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfcf9984-3393-3a0e-92e6-3740e0ccd73e | -9.1323 | -65.9474 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2535105d-bc84-35f6-8300-bf086728b946 | -10.08943 | -59.16615 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5481d996-479d-3890-8b38-90a87cdaa280 | -9.05739 | -50.46595 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 115a5391-fff2-35ce-bb1b-0717092e569d | -11.18366 | -55.0571 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ea6e598-18c9-3560-b9c5-0d55aed99953 | -9.84552 | -48.85833 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c231729e-204c-3b49-be4f-dae4617ff37b | -13.83088 | -46.2421 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc401ab0-6dab-3ed7-af42-81bc795a1d59 | -7.10765 | -63.06964 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e9722e6e-7844-3494-88c7-0369f0a76b36 | -7.08289 | -45.19651 | 2025-09-08 05:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d943b06-f68b-359a-b927-5a3a460eb026 | -12.63833 | -56.97868 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbee537f-b30a-3758-b355-04cd08aef931 | -12.93171 | -54.77778 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 997b9a7e-526e-3a4f-965a-f2a405f03f22 | -10.22077 | -50.5226 | 2025-09-08 05:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8fd8e3f-b32b-3764-b89f-002504f772d1 | -11.21342 | -55.02104 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40ba412-5f55-34ae-a5e9-631529c5b8c5 | -11.20035 | -55.05514 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99804501-2f97-368f-8975-d19c3964c29a | -9.14469 | -46.0647 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 659508da-0e47-3b30-8fd6-3ae426054b29 | -10.0007 | -51.6389 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d29685da-b84a-3bb5-ae7b-03becfccf4b9 | -11.91301 | -50.98647 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df3596af-bd8a-3984-9d06-e1530f5f3c08 | -8.18894 | -50.143 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cab1951-d641-34cb-b111-0b85f4a36007 | -6.27699 | -53.4452 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203d1e1a-ce8f-3d8c-94b1-c8109359b1f3 | -12.94324 | -54.78735 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d54f564e-17c3-3dec-a87d-76a040eacb67 | -9.19979 | -46.0433 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9a1080c1-1c53-3687-83ef-1f0f22b5d368 | -9.8541 | -48.83829 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84d5b2b3-4f57-3fb0-9b40-c5b5b98e7238 | -12.83399 | -52.904 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd27afa4-f001-32d7-9783-9623d2ff0633 | -11.0287 | -45.94841 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad84ac0c-49e7-3930-a64f-eb55d518cd5e | -10.00342 | -51.65686 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c32a85-6f74-3a3e-96f6-954c977d33d0 | -9.17499 | -59.37731 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba024f8f-4203-36ad-b3c9-913529eba77f | -11.86771 | -51.06433 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 521a1dcb-db51-31df-82f2-30ad9d57b940 | -10.42412 | -60.75128 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee1ea05e-a0cc-3a09-81ba-cff74b32a608 | -6.83429 | -52.79766 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 820fe73c-094e-3cf5-881d-8d429f807a56 | -10.58319 | -61.23603 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad90a0f2-ecbe-3fba-b477-95c241ce3f0a | -6.84101 | -52.8446 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a96c6b-0f6e-33ea-875d-b8d2296f4d4d | -12.62608 | -56.98575 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82685bf6-b9fc-3240-85fc-7bd8fb6904e7 | -10.09002 | -59.18433 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbe64042-afeb-3136-91f3-52ec8ab82b3d | -9.87522 | -46.52994 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4feed8c5-8e13-39eb-abb1-dbbcea81969f | -12.1959 | -53.90865 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a83b64d-9561-3f86-885d-413816f118ec | -10.15517 | -61.14005 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1c5d9a9-0df4-37fe-98de-cc1e6b0152e8 | -12.95268 | -54.78078 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c99161fc-072f-3c8a-ac65-6f7f19d23d0a | -10.28658 | -48.80927 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0cdfed6-6a22-3ed6-85b3-46ac0ec0b09d | -7.59768 | -61.5931 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 27ceaed7-8908-3d1a-83f0-79d522567f95 | -6.5299 | -49.49729 | 2025-09-08 05:21:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 126c4d32-0fa0-3166-bea0-49f1a4104154 | -12.94169 | -54.76732 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42043acf-7505-35db-b02e-322807bd685e | -11.61116 | -47.14679 | 2025-09-08 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5daae6e1-76b7-3ee6-b786-441f0330fa92 | -9.84678 | -56.04208 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85407e07-3486-3c56-813b-949afd8d74a5 | -9.81765 | -53.31752 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02103c8e-1209-35f8-bde6-adf4a3c744c2 | -9.17332 | -59.36628 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb219624-9462-395e-9bf3-0b10919fb6bc | -13.8108 | -46.29521 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b95b71e9-709b-307f-a4a7-45a13f26a3ce | -11.8624 | -51.06357 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4cae72a5-54fe-352d-a1ac-ec8d64d596fb | -11.41139 | -50.39166 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ed431e0-2e2c-3682-998a-925a7ebf4adc | -10.95848 | -46.81886 | 2025-09-08 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3c4d4b23-6678-3636-999f-f5437dab9321 | -10.79896 | -47.72892 | 2025-09-08 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c702293e-b25a-335c-bd23-5d46b94f3acd | -9.58642 | -48.2953 | 2025-09-08 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4faaa92-e375-3d76-9f44-31964f932297 | -9.99452 | -51.67934 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9a0034c-7242-303b-9d11-ef8c2573ed52 | -7.78563 | -52.12931 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e69453f0-b2e8-3e45-921f-a207564f3f6d | -6.84855 | -52.85436 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 665fed77-8fcf-3285-831c-dc34cdf3442e | -8.70341 | -45.31038 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89053de-accb-3ea2-8931-e0a3629c1835 | -10.58039 | -61.23187 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c1a284a-ed6d-38a0-9b62-a6c047feda68 | -7.4011 | -61.6264 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 82864d7c-c15a-3469-819d-c41005f2eb61 | -9.24957 | -57.0628 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf64620-b4fe-38dc-ab68-60266b54dc32 | -6.95248 | -62.93518 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bee1b2a-7db9-38fa-90c1-289d8785e1a3 | -9.44452 | -61.82613 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf53e091-077f-3713-bb57-25211c848be4 | -9.20046 | -46.05468 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 69627af8-d7c0-351f-9ed7-4abe1b19c14e | -11.41465 | -50.36614 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85520380-d7cf-3aba-a489-95eb947f28a0 | -6.27203 | -53.42127 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1eeb289e-ccc2-3d18-b327-20245033c837 | -7.89932 | -61.78097 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README86.md)
