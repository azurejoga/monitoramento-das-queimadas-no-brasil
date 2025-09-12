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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 442993ce-1869-3833-852f-59bf473a0991 | -6.76849 | -41.59259 | 2025-09-12 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 400faa1d-3939-3dd2-b7f2-6e1933d6da60 | -9.89126 | -46.46503 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b8cc6455-38df-3ce0-bd4b-d23145707e9f | -11.67298 | -46.56741 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e22107c-2b3f-33fd-b586-908ee302985e | -8.37425 | -47.59999 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12e3d241-b636-3a0a-bcbc-745603c147dc | -8.87866 | -49.54205 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a4458c-c1c0-305d-95de-6b3af3ad78ee | -9.89129 | -51.87235 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f277e733-87ed-3207-897b-bbe04836be03 | -11.08388 | -48.40992 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e30d642-7cd4-3339-a4a3-46e812224824 | -10.08321 | -47.16128 | 2025-09-12 04:04:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bdfb2d4-6352-3729-8bdb-ba86e13cda14 | -6.12593 | -43.2913 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96dae25e-6987-307f-911c-da92d1f34800 | -7.4467 | -44.44069 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d012f58-65d5-3130-a69a-35e4f510be3b | -11.68433 | -46.52642 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a9caff-7bfc-34a8-aa1f-70760a11df84 | -6.65631 | -44.13214 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0f69a2f-6b9f-3034-873c-669280b57655 | -11.69497 | -46.57408 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02ded8b9-a127-3f45-9d63-934081edd52d | -5.76542 | -45.52347 | 2025-09-12 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e07484c-4619-3bd2-a3e0-fd7570848608 | -7.07823 | -44.14944 | 2025-09-12 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c7e1dd0-246c-3ec9-b6be-6ff473f2eefe | -11.14398 | -45.2345 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 525bab06-9920-31ab-aba8-4731357d3234 | -8.4781 | -40.66634 | 2025-09-12 04:04:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc02c540-b770-321e-8653-3dcfced05c3e | -6.68922 | -44.13603 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a70c01d4-daef-3fd4-865d-c9cd2f30b854 | -6.28133 | -42.40424 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6ef25e6-3d93-3f80-a938-a76faedea737 | -6.30615 | -42.22847 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b708aae3-e78c-378e-8957-11aa561c58b4 | -9.73594 | -45.42587 | 2025-09-12 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2960acd-c2dd-37d2-bd24-db61afead606 | -6.44353 | -44.03894 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6409fb7e-77e9-3baa-bbe0-73da1f7e3779 | -10.12526 | -47.91312 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1f1ee4-0c50-3a00-ae1b-4c9cb5de7167 | -10.56393 | -43.6624 | 2025-09-12 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fda73499-f354-3d1d-bc73-d192217a34d4 | -6.96986 | -44.82767 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70c990dd-bb97-3994-909f-0cf9c4f782df | -10.556 | -51.48774 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 431b74c9-1687-369c-b9f7-c26dbb00ef04 | -6.68157 | -44.13466 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8a27e0e-d154-371a-9723-40c1db18fc49 | -11.67517 | -46.57941 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0da20ea-b5f3-3e48-bd6c-6d702191a299 | -9.08462 | -46.95452 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ce99a6-5556-39b0-b91a-f9175f943be2 | -8.18384 | -42.42532 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80febaa5-d517-3448-8dd6-e488e1d2767a | -9.51177 | -54.64139 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6df27b8b-7b29-33d4-bbf3-b4e08f3e5407 | -11.43304 | -48.56853 | 2025-09-12 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6e52dc9-bd3c-3a94-9309-8e4441646151 | -4.94611 | -49.92794 | 2025-09-12 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be4dd508-1cfa-3ebd-8301-844c39fa6dfa | -6.96674 | -44.82182 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f17dbb1c-3c96-3b45-b340-30b0b46729b8 | -5.49437 | -42.67901 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85dfca0d-249e-3594-9ead-7cb5ab3f3626 | -6.31727 | -42.22625 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d41b3cdf-6e83-3b45-bb7e-3da10a561e37 | -12.10536 | -44.87874 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed98a656-4799-387d-8152-40acd57aadfb | -7.4573 | -44.92596 | 2025-09-12 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 842b7f6a-7939-3c51-ad22-7b48a63e4dfa | -7.45322 | -44.99856 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7204360-aa1d-3ae3-9d01-6864aea31786 | -10.12197 | -47.91546 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e89bf8f3-57d6-3fab-9db9-2e7089879d1e | -11.18236 | -48.35691 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d0cce14-c49c-3f41-8947-5e2acfcc1d5e | -10.20144 | -48.15936 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d6633ef-c702-371a-9b2b-c597e363028c | -8.57821 | -51.34986 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 201d9f09-29b1-307a-bec4-e6da968432ef | -10.35866 | -46.3903 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab7499f0-89c0-361e-a5a1-8a2305b8a46a | -9.72089 | -48.34434 | 2025-09-12 04:04:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a1cb2ae1-b3d4-3d56-b148-fb766e0af7a1 | -6.26733 | -43.34412 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13bff406-d0de-355a-b8b8-24388e27105e | -11.67056 | -46.60603 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a840ed5-b1a3-3115-a7cb-f23bdf1df11d | -9.72277 | -51.00469 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fcd3c2b-685a-3dc5-ad02-144f2e507825 | -9.77954 | -47.86007 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec9d5d5f-0da0-39dd-bfc3-4fb72f627989 | -5.28977 | -48.1285 | 2025-09-12 04:04:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20ca4716-7706-3da6-b998-d87375b24dae | -6.68077 | -44.13939 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba630fd5-8c66-3d19-9dbd-6ef6972819ae | -11.67429 | -46.55986 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b650301-d9f5-325b-80b3-1ddf09805ae3 | -6.48547 | -43.87874 | 2025-09-12 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a351eb7e-3789-3418-9cde-1b912fda4f3f | -8.18509 | -42.41775 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a807076-b011-3f04-88c7-21fc503a051b | -11.15008 | -45.2976 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3b7dac5-3cb3-38cc-a327-5c320af640ae | -8.73666 | -47.11863 | 2025-09-12 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6501a54-45d2-3302-9452-60c454c32ef9 | -11.15824 | -45.31908 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d86d1ef-d756-3c75-b3a7-5d028cdf4f61 | -11.67168 | -46.57493 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a84f39d2-176b-335b-a024-3815a52220f2 | -10.83385 | -42.75889 | 2025-09-12 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2da1ca27-841b-3ad6-aaf2-c9bff89f29ec | -11.23919 | -49.41132 | 2025-09-12 04:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42556f1b-e942-31af-bbf3-050ddddaf6f3 | -11.44306 | -48.56676 | 2025-09-12 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 283cf131-1f25-3acc-bb40-f6c37bb1aca9 | -11.43667 | -43.56397 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5195b342-fc07-3d4c-a67a-12568f827818 | -6.18344 | -41.08025 | 2025-09-12 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b321de0f-fcc3-3a5e-97ee-cef270fab04a | -11.68397 | -46.58778 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d9f4c62-0260-3a4b-8235-68050b1e0ef8 | -8.50515 | -45.65689 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d01c97eb-bc22-3698-a795-7070b9894f11 | -10.67367 | -48.59106 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 06343e9a-92f9-3ac0-9af7-f3a8a7e1688c | -12.12112 | -44.85381 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9c66702-dcac-3c7d-88c2-643aba8a07ef | -10.88973 | -45.59309 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6a9a960-24a7-3ee4-82fc-8c5c6161c834 | -8.88126 | -49.93804 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 682a7b85-6fb0-3260-b32e-621265edfbb0 | -10.95431 | -42.89848 | 2025-09-12 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1dc8fc0-9e8d-358e-b12f-f715b73e2477 | -10.67188 | -48.59435 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 32181987-bcda-3d12-93e1-914f3bfd73a6 | -11.67641 | -46.60602 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abc22adf-0775-3434-971d-5a5b8a35591a | -7.31916 | -44.166 | 2025-09-12 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b3a2334-67da-3aea-958f-6b33bbb05324 | -9.84387 | -43.54406 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788e1d3a-5110-3fad-a418-6e0705c398e3 | -8.18555 | -46.10844 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 564d9711-cbab-35ec-8bed-189a81bef559 | -6.24718 | -44.79862 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57962b74-1119-3c99-ad9f-b8b0290493f9 | -6.81208 | -45.64343 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f1e321e-8d45-33ef-b636-12e186972a29 | -8.18163 | -42.41715 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 241eb0a3-bcf3-391d-b709-55d226d1bb70 | -8.18039 | -42.42472 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9599e35f-2dfa-3ee7-a202-be68a21a35bf | -6.18287 | -41.08384 | 2025-09-12 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| debd9222-c015-3db8-9c64-6de6764c5669 | -8.87809 | -49.53459 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9933d99-7691-305b-ada7-b7d516303d73 | -9.52045 | -54.63497 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 284a8685-6245-3847-a5bf-1ed928e2191e | -11.87239 | -44.76613 | 2025-09-12 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27647eb4-a114-38b2-adca-d1fdae01f1d3 | -5.51856 | -42.69458 | 2025-09-12 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d890e6e-005c-3981-a11f-78497562d998 | -10.84586 | -48.15996 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3b72269-71d1-3378-9fda-be05b424b9aa | -6.44548 | -44.78176 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0749bd8c-eb23-3a2d-a61d-ea97914957ff | -9.85441 | -43.13189 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d71339e-4b80-3156-b2ea-3a810c776c7f | -11.66946 | -46.62082 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2caa10ac-d02e-3c42-8ff7-e5449bf10c5d | -7.21917 | -43.97578 | 2025-09-12 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06a66cbc-8fc7-396d-b5e9-c27c0cc411c0 | -9.71802 | -43.51562 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b6990eb-44a2-3d8e-814e-db010cef8b7f | -12.13455 | -44.84224 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1638613-0094-3106-9c7a-36951005fa67 | -9.72203 | -48.34737 | 2025-09-12 04:04:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27c484f4-2ac0-3d4b-b234-502f3d49ac6e | -10.70753 | -48.61689 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66167762-a624-31d4-9b4e-553575d36c62 | -10.4225 | -50.62646 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7440c250-4ef6-3391-afe8-c3febd4ffcd4 | -10.37138 | -50.51076 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24d69d53-4475-32ed-8418-32fb6a3de059 | -11.93476 | -44.30448 | 2025-09-12 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9c0a044-1169-35a7-bd65-ca7ceb9035d8 | -11.53384 | -41.91343 | 2025-09-12 04:04:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a078613-fbe7-3dd9-9ab5-99777ef85e61 | -11.56984 | -43.23778 | 2025-09-12 04:04:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b07a1c9-6b76-37a0-bc42-5ed7893df53e | -8.33416 | -45.41867 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da80025f-09db-3cf4-ad1b-15774e2d56c2 | -10.48085 | -49.37302 | 2025-09-12 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README33.md)
