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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e37edfe9-cd90-3733-a411-4061c3ffe392 | -8.55303 | -54.59298 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55858c5-abcf-3051-89ca-b08cca8895be | -10.59066 | -55.5937 | 2026-08-14 05:53:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fae500e9-0adf-38b5-bbd0-7fe5eb04dedb | -8.95276 | -60.53587 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ae50c82-09b5-32b3-918f-5c38959cd3c4 | -7.37975 | -59.96664 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df268171-fd68-3fac-a755-0c2a46288d29 | -10.94323 | -57.12574 | 2026-08-14 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbedc960-56bb-3d85-ad59-4fc141548b41 | -8.9533 | -60.53208 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed6b6cb4-e011-3f68-be18-67e8bb0b0a91 | -9.75073 | -60.76219 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2884a2c2-9862-3244-bdf8-c3f789d6d056 | -7.55369 | -61.16988 | 2026-08-14 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c9b9be6-d22b-34e1-8ab3-117d058c5d02 | -8.96546 | -60.50663 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c04c53e-6982-36bd-9eb7-ac3f97b74a75 | -10.94279 | -57.12918 | 2026-08-14 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768ae061-cf58-385f-9c13-5dd392d966e2 | -8.96073 | -60.50985 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3831de9c-08f1-306d-9ca2-a92b73c47e9a | -7.3749 | -59.96888 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 774eeaa1-7503-35a8-96dd-0d3299a07e66 | -11.49523 | -54.61359 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e47b0299-a665-38ad-83ca-7736596822e2 | -8.72003 | -54.60182 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19710c19-be1b-37f8-9943-11a00adf9b7d | -11.61663 | -55.17861 | 2026-08-14 05:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61dfa1a2-20c3-3cb9-8d86-de188f7a4537 | -3.24283 | -60.12794 | 2026-08-14 05:53:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce09f904-a1a5-3841-81a4-ce24a1938284 | -9.73442 | -60.74927 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01cfc833-727c-3092-a938-0dd666054d01 | -11.61604 | -55.18348 | 2026-08-14 05:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a23c90f1-3923-3107-81b1-c5a22c00d9c1 | -1.83154 | -54.49721 | 2026-08-14 05:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3b13d842-e1d1-3167-9d33-071a090a72b7 | -9.75798 | -60.77093 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310b2595-9a11-3265-81dc-4a9c75207dfa | -9.58521 | -60.50124 | 2026-08-14 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d92531d-b719-381b-bcc0-8bc7f147b0b0 | -8.89317 | -60.55899 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8fa765a8-6a18-3983-810a-b4c290f39f0f | -9.75746 | -60.77467 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95ebf02a-badf-397c-a2cb-1a0bd5b39720 | -11.50869 | -54.60962 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78b21cd8-02ca-3a13-945e-c5eee9d236b9 | -8.95747 | -60.53271 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb9848d-05d1-34e1-a773-fdc226813b4b | -2.73597 | -58.18928 | 2026-08-14 05:53:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d40a79-1a2c-32cf-a62a-6541dac5fcc9 | -11.48598 | -54.62268 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65e7c57c-6e45-38b7-8199-187c652230ff | -9.60823 | -66.18499 | 2026-08-14 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9773d2e-39c5-32ad-b8b2-ee3c59a46188 | -8.89732 | -60.5596 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e19c982a-f187-399c-8eca-355f1e5102ea | -6.98097 | -63.01241 | 2026-08-14 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 117007c5-d3cc-3eb5-9072-25c5b3d49f5d | -10.07978 | -60.49925 | 2026-08-14 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 306840a2-16ac-3c65-8948-56f772466ba3 | -7.40591 | -59.99349 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bc5657-8bb2-30cf-9d52-630429d73595 | -9.60491 | -66.18446 | 2026-08-14 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72d58c6-98b4-3e61-9590-52b8110aedff | -7.58944 | -61.22581 | 2026-08-14 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db74504b-de2e-3512-b38b-0ee83785e2cd | -9.98287 | -53.95407 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6e402f13-3963-3075-8bf6-6685bea2d70a | -11.62223 | -55.18428 | 2026-08-14 05:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13ded1f1-8e02-300c-a562-85bfbbe459ab | -7.37916 | -59.97056 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958ce923-05cd-3030-adcb-427ff00d1a2a | -11.48536 | -54.62783 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2767235c-a2cb-3947-a209-18cfa11d994e | -9.77036 | -66.61316 | 2026-08-14 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 790761c2-b810-3a62-a335-2fbeadc7b24b | -8.02305 | -55.11666 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e35aaeb5-4514-35a2-92d7-6bbe0dcc0fb8 | -9.98231 | -53.94524 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| fb17982d-11b5-3fab-aa48-175dd0aa9ef4 | -8.96128 | -60.50601 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87374777-61a9-3dd3-8996-90dbe39cc924 | -3.24361 | -60.12293 | 2026-08-14 05:53:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5642b4ca-dd44-303a-8fac-14528301642a | -11.48702 | -54.62861 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e293d737-fc05-3c54-9b80-9b6d4f7a41ee | -7.38079 | -59.95776 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 324a8f59-0073-3c22-a81d-5876ff096dd6 | -11.48821 | -54.61821 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b4cf0ec-d66c-3d68-8cd8-c834ea79155a | -10.59659 | -55.59462 | 2026-08-14 05:53:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954d6c83-df7f-3a7a-add0-81fccce5b4b6 | -9.58466 | -60.50515 | 2026-08-14 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcb0686b-f1a7-324f-a7f6-0ab141c1ac5e | -8.98246 | -60.53646 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f1effe-feb6-3bd8-8151-f91c1efb2b18 | 2.60814 | -61.42968 | 2026-08-14 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d39122cf-14b6-3ab9-960e-0310d00b8bdd | -8.02246 | -55.12107 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae29e777-1206-35d3-a578-ce75b69bb65f | -11.49881 | -54.62405 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 302178b0-5739-34a7-a5ad-5d17b6eb4f0b | -11.49176 | -54.62857 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7dacd230-2b61-353f-ad9e-c29c78d1ca23 | -9.7684 | -60.75706 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49533c23-f932-39c9-83a9-069b84aea8ef | -9.98164 | -53.95085 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f76d311c-2815-3bd8-9d48-2499b9e9260e | -9.83252 | -65.06084 | 2026-08-14 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff19e37a-370c-3577-a393-f9587fcc7ac7 | -3.15441 | -54.60303 | 2026-08-14 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3395e1e-ac60-321d-a8e9-a6bf28a097db | -9.7601 | -60.75582 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d53cdaa8-4996-3048-a7ec-fe1b79151129 | -8.55241 | -54.59781 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aa9b564-45d7-3cd3-9b3c-e03d46325451 | -1.83095 | -54.501 | 2026-08-14 05:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58e79171-4e84-3e43-a83c-53854b7e656c | -11.48761 | -54.62346 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 184c5bfb-62a7-333c-a471-ad8dc4e23ba9 | -11.49864 | -54.64046 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1246e49f-b462-3878-b058-95e7aaa19152 | -7.37434 | -59.97286 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab9fad5a-b6ac-3bba-9156-31a2becbbd55 | -3.19481 | -54.44904 | 2026-08-14 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3376c6da-3ea0-31be-93ec-70b0968de7bf | -3.18797 | -59.01121 | 2026-08-14 05:53:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 598289b8-d700-3be7-8d41-94d9882984e2 | -11.49402 | -54.62415 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a997e0b-6b99-33ca-8f36-4994c94465b1 | -8.72067 | -54.5969 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91514da1-a706-3d12-8094-8c36539774de | -11.49303 | -54.6181 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0d19be3c-4480-3fa6-8480-eb2788afb103 | -8.96109 | -60.53712 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54d1f95-274b-32c4-a3c9-0838894aa49f | -9.77149 | -60.76522 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 958db2dd-5506-38e1-a88e-0833a4357415 | -7.37912 | -59.96955 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17259193-1584-3ffd-b403-13b79513653d | -9.76425 | -60.75644 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ccfcc40-f73f-3002-8b66-4a1c251adb24 | -7.40956 | -59.99808 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5152e1f7-43a6-37cc-97cf-0b50f2899a8f | -7.37553 | -59.96595 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49dd9b4a-8b01-3991-914a-949aae3c4c8d | -8.95601 | -60.51308 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cf37d7b-7280-3f16-81b7-8d7e74783d71 | -7.48897 | -63.76796 | 2026-08-14 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d09cb9ae-3d89-3e0c-9f6e-cd42d0625da8 | -9.98217 | -53.95973 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 81afec62-a702-375b-af5b-3e73003d754d | -8.89787 | -60.55585 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f93b23e7-612a-3115-b9a4-6e539f010a52 | -11.49284 | -54.63454 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 840c8228-73a9-30de-bd45-875d0e4ead49 | -7.37968 | -59.96562 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 722a41ba-8e4b-36df-a459-e71b271f882b | -9.98817 | -53.95185 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dad5d62-f5c5-35ba-b47b-d56e0faaa412 | -9.19512 | -66.10066 | 2026-08-14 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c043c6a0-c91c-3cda-a77d-4e512301d094 | -1.36953 | -60.26557 | 2026-08-14 05:53:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b97c16a-9630-3080-95c2-c0f455704442 | -7.37494 | -59.96991 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40b65029-8fe2-361b-8963-fdc0742dca3e | -11.50044 | -54.62486 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c88f004-5130-3f96-a6fb-b4d64cef12f4 | -13.83375 | -53.78739 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abcbd50a-4d70-3710-adb4-b1e9e2f17f93 | -6.60645 | -56.32986 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67abaa4c-8e27-3947-b84a-78652300fe60 | -12.51939 | -55.78601 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4533b8-2c47-3b6f-8bf6-c0dca40a18f1 | -14.07413 | -53.61932 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b46d6da-2be1-3c2d-b857-259d73234530 | -6.60392 | -56.34745 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7890e482-7381-3c26-8b25-db8be6bc8c2d | -11.62165 | -55.18013 | 2026-08-14 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af9470d6-6ac2-3ab1-b225-43557c7ff6c9 | -6.60792 | -56.3406 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361c2299-3e57-3880-9e7a-a37ff014a594 | -14.31541 | -53.0691 | 2026-08-14 05:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3a1c306-842a-3678-828a-c47f44b0dede | -6.6211 | -59.04177 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a6785b9b-9cdc-304f-a625-7423057fd713 | -12.51755 | -55.79171 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abdc51a8-941c-3a86-91bf-d31c44634b4f | -6.60164 | -56.34657 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d46bcb-34b6-34a3-8262-46fd8253e939 | -14.06079 | -53.61136 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f796926f-f7ae-30d3-a8d4-6e648ca032b3 | -13.27937 | -54.21341 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b9eac5d-bb0f-3526-a912-ce13531c17c9 | -12.52357 | -55.79258 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 460a9aca-de09-34d2-baae-bbeb3b8b9ce5 | -6.60697 | -56.34759 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
