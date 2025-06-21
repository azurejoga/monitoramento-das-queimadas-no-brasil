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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 714d7496-134d-38c2-ac35-04bba4cabdd5 | -8.01701 | -47.66531 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d7f0c17-6d5c-37e1-810d-14f382b83244 | -9.47113 | -57.84344 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8770109-c77a-3404-8630-246fbedb5fb8 | -8.67686 | -44.30073 | 2025-06-21 04:59:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8352700b-9de5-3c38-983b-9104bf15d391 | -12.26484 | -44.6044 | 2025-06-21 04:59:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c525d83-060e-3f63-8608-c32529269735 | -9.41024 | -48.43343 | 2025-06-21 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43b28d93-ffc7-30b0-b266-3bc2d4e499d1 | -10.03281 | -54.32332 | 2025-06-21 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8c7b71db-f1bc-3e7b-9225-a2a37cdfc711 | -11.10622 | -46.68767 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1672d984-8e7f-30f4-bb46-ecc7e8e5e039 | -11.07949 | -55.05299 | 2025-06-21 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ac212c1-9c9d-3a7d-baeb-967aeb4ec059 | -9.73577 | -48.33312 | 2025-06-21 04:59:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f648ef0e-33e5-3bd9-99a9-ea3f37fa5725 | -9.25318 | -57.52721 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 659cd2ce-3ef1-3e0a-9d0b-b6109a7bae85 | -10.29543 | -57.13649 | 2025-06-21 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c206733-fcda-3eae-82c9-2046e08ea458 | -9.249 | -57.53059 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38fc9196-49d8-3886-bd41-f90407b7c730 | -8.01176 | -47.66933 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd78e4d3-1ed4-353a-b474-3d33ecd66c16 | -9.01215 | -61.22765 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63cca26e-eb21-36bf-b3f9-84f87414a1df | -11.178 | -46.65995 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17ebe3dc-1cdd-3ea7-b626-f45973a9f258 | -10.93713 | -55.33282 | 2025-06-21 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62493833-72e4-3324-ba0d-a1d1fbf70cd8 | -9.40578 | -48.4328 | 2025-06-21 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef580881-477d-329b-b4e8-7fe820f77fa7 | -9.26204 | -46.90219 | 2025-06-21 04:59:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98177d9b-c13d-302f-b4f2-1b2bb1bc312f | -11.17404 | -46.64998 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a210b7-e1a4-3a17-8842-16a06771d449 | -7.21845 | -43.06456 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 81ccacea-ab6e-3927-afbc-bda1029d8317 | -9.45752 | -57.83693 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f17eaea-5ce8-3bf1-b9e4-7398a9b0851c | -11.14077 | -53.91822 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 783437f1-83a9-3408-b2af-17c378d2a0fd | -8.01307 | -47.65992 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c53c3c8b-ae4b-390b-946b-87baaba47179 | -8.02293 | -47.65664 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d3ca56c-9fab-3bd5-b8c2-11297c95d83e | -8.38123 | -46.97354 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbd14c39-9d15-3523-a3da-dce4facf0c6d | -11.10479 | -46.68415 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a48284bf-3881-30f7-bdfa-2b813ee05177 | -7.22078 | -43.06342 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 76219f19-d6cc-3642-810c-50e8bc3db82d | -9.4725 | -57.83524 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af511b02-7e6a-3b69-a39d-c83717f243f1 | -9.74026 | -48.33393 | 2025-06-21 04:59:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dfa3be8-d307-38b4-a2cf-afe7bf9f0ac0 | -8.37714 | -46.96739 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1167eb0a-17ac-3832-bc1f-c32f5fbed3c7 | -10.44882 | -47.03321 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 365c8f8b-c692-3a0f-a3ac-85a903bb6f1b | -10.86884 | -53.75986 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d37fbc-810f-3e0a-a016-901fcbac46e5 | -11.93735 | -48.42589 | 2025-06-21 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8f572d8-bffa-339b-91d6-e3926e98749f | -10.14724 | -48.98733 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa9a24e0-4543-34d0-a0fb-a8e5be7dadbf | -11.17444 | -46.64688 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ead38c8f-16bb-3902-8bd3-fedadf8e6e6f | -10.866 | -53.75566 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21675d44-0855-3a7c-af45-d94180ae8ddf | -8.02227 | -47.66131 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33214e6f-eba9-304a-b4b8-a5f12967880e | -11.28895 | -46.66247 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84c608a7-52d7-33f9-89c4-d3d74682fca5 | -9.25253 | -57.53119 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 309b32c5-a23b-32e8-ae43-3e5f2de27e22 | -10.15064 | -48.98521 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d6775e7-bb93-3550-b639-9420efe09f96 | -7.22012 | -43.0682 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2ae009a3-a030-3c2c-baa3-c7575695533b | -10.44236 | -47.04382 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4042741-c459-3349-a09d-48a3997b407a | -9.46686 | -57.84692 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3cdf42b-13be-3a33-901d-d353a4c3edb2 | -9.02099 | -61.22913 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb8d3c19-79a1-36bc-93b8-76038bf40627 | -10.8863 | -54.75167 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeef2880-56d3-3d19-94ef-178a72fd9b9e | -11.8853 | -54.6722 | 2025-06-21 05:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d7d2fa31-f8b7-3116-a6c2-c658d35d15db | -11.8663 | -54.6739 | 2025-06-21 05:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| fd18ad0f-5d88-3562-a99e-c6ff697cacce | -11.7791 | -57.2445 | 2025-06-21 05:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9d5f46c6-d8a1-3af5-b339-cf3011eb2366 | -11.798 | -57.243 | 2025-06-21 05:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 433408e9-23d1-358c-ac38-c229cf142459 | -14.22386 | -45.51668 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8fcf78-5f8f-3a31-bc4c-62e2b12ba0c3 | -10.8874 | -56.46306 | 2025-06-21 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6d85bf81-08a8-366c-bc13-f0ef82630f0d | -11.94785 | -58.75547 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fce91c39-6467-389f-9721-1ac637d61fbf | -13.89792 | -54.63659 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ada415-a7ea-3da0-bbd1-51ffc44e70ea | -13.14159 | -56.80521 | 2025-06-21 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 024e340b-003e-335d-8c2a-86bfbbe68a73 | -13.03928 | -53.71554 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5a127f42-48fd-3dfc-9eeb-928ac2915bd4 | -12.52339 | -57.20938 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ea0164-f771-3eb4-9110-cf3adaac9dba | -10.23389 | -64.35728 | 2025-06-21 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f095995a-738d-374f-afc4-69de3c54f659 | -11.79158 | -57.24151 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 52695553-9243-376f-84f4-cb7f4a48de2c | -12.28612 | -50.10784 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26db404c-367a-3115-951a-2598037f80ba | -12.57266 | -58.37091 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d33977e-a1f9-3b4a-b6ea-7047a24fbcc3 | -11.94494 | -58.7506 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caae757a-faf4-3128-8e9c-be138f4d7938 | -12.50763 | -58.35278 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c146c711-9bfd-3a15-994f-47ba26f0a2c2 | -11.52696 | -56.97706 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 466e7f41-6ea3-39f0-b715-53b348cf1fc3 | -12.5698 | -58.36625 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f35507f-acdd-3172-a64c-d3c70f978bc6 | -12.28248 | -50.10343 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1001f5d9-7965-3423-9924-7a2585667051 | -14.07413 | -53.38069 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0ef0200-e87d-364d-bf5e-6de5fb8f6a62 | -12.51999 | -57.20881 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f8a2127-b132-3400-9382-8d47e39db625 | -11.91676 | -54.82042 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cad5d8db-e95f-351c-9e87-8fc881a4b369 | -13.24048 | -49.84144 | 2025-06-21 05:01:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 549224c4-4146-3388-a4fd-2354031782fa | -11.77408 | -54.36504 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efce0db4-8051-345d-8464-4439ae467f26 | -13.36243 | -54.25913 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a1b0911-0e0a-3af1-9e6c-62a1cde7aa2a | -14.81245 | -48.47141 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c3e271e-5675-3b7b-9190-112069791434 | -11.78878 | -57.23717 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a5ab62eb-6ceb-3cf1-94f0-3a36d209692e | -12.97282 | -54.68237 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e81f8741-41a1-3e6b-8848-825444fd4250 | -14.02939 | -53.36675 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e08441b4-5fd9-3ceb-8ea6-55cbd3a0e3e8 | -13.0433 | -53.71223 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 32db2528-9155-372d-85b0-8d3f56d3392f | -13.03985 | -53.71169 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 79068793-d038-3dc8-8036-be327246f601 | -10.23328 | -64.36063 | 2025-06-21 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fcb54f9-399a-33b3-b1a8-4973c83c0479 | -11.87698 | -54.66472 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d531ba13-d1a7-3563-b737-d67f128d9ebb | -14.02526 | -53.37024 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7e10c23-b4f6-34a3-882e-f4f886b3d8f9 | -12.02994 | -57.08644 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad649f3e-a97e-3bc6-9974-0a7c10fbcc08 | -13.89339 | -54.62078 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0789b012-3f89-31a6-93d2-9d1084582286 | -11.87978 | -54.66882 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5137ea7a-b020-3419-b144-0453d9304a47 | -11.52756 | -56.97338 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ddd4f6-879a-3acf-9cf6-046fcf1d3695 | -11.6564 | -60.1212 | 2025-06-21 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab1d57f-b60b-3a87-9e3c-6203318943ad | -14.81112 | -48.47215 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b343d12-02df-34fa-9335-dcd2d1632ef8 | -14.96512 | -46.26245 | 2025-06-21 05:01:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 793f6302-e58c-3fbf-86a2-dafb8f4a2e10 | -11.81172 | -57.34841 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85931f0a-7cdb-3c19-ae4f-907e0217f6ff | -15.77032 | -43.27009 | 2025-06-21 05:01:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b9a3495-38fb-3956-ad14-8cbc48483dca | -12.5777 | -58.38435 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72c1ffd2-1d33-305f-ab4e-29591b6eed41 | -11.795 | -57.2421 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e5c6391d-a61b-3564-a5b8-94e1eb7675d9 | -11.78817 | -57.24092 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5646d3ce-8196-3fe1-bc1a-c7593a426e78 | -12.65002 | -54.13021 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57607409-07ba-36a4-a6ef-62776519c926 | -11.53095 | -56.97394 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a180cb03-6c28-385b-9b94-be87392029a9 | -11.78352 | -57.24787 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b61cf497-35ac-33d3-adac-5386a5837634 | -11.77352 | -54.36865 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec0759a-b7f6-3c1c-9058-8d29fb41ae8c | -12.9689 | -54.68545 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 052e8cd1-be63-37c1-9d09-9af9c8e7080b | -14.22935 | -45.51924 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3090c89d-fdc4-3b7a-a77a-17052c2aa520 | -13.36979 | -54.25651 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d195b6d-4295-3142-aced-2ae0473921f1 | -12.50679 | -58.35116 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
