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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a5df071-3548-324d-bb3e-c8d9fc313c5c | -7.95779 | -46.39267 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 920859a3-057c-3939-ab9f-2a84470befdc | -5.99977 | -44.71966 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4adbfb8-d73e-31fc-a9a3-c37a79f56c70 | -4.37699 | -48.06843 | 2025-08-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc23d24-65c2-329f-88c9-005bab277c5a | -6.36303 | -44.46241 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e8aae9-8ca5-32d1-bf67-a5ad2599b0b4 | -6.77911 | -44.82862 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 026208f4-76eb-3faa-b550-c1082dd6fa50 | -6.7861 | -43.77584 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad005b46-80db-3c32-a90e-c1e5e47afb4d | -7.74647 | -50.26944 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e56f005b-0203-30a3-825a-b31c77073b31 | -6.55776 | -43.69041 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e6bf308-6881-3a2b-8e73-d895a1970efe | -6.56413 | -44.22021 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6adbbd74-c291-3ef4-93fe-3cc86d8d3d64 | -5.61822 | -45.00556 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9af07487-8088-301a-a5e0-8bf767ab5a33 | -7.78133 | -45.4662 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 262eca96-7f20-3c6b-823e-238c1c4033bb | -6.29877 | -42.79446 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5ae423f2-da82-3c8a-900a-229b6823b999 | -5.58938 | -46.33006 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ac9eeda-774d-3d0b-8072-16df3eb35b55 | -2.98532 | -48.60224 | 2025-08-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37d03833-a642-38e0-9e51-a20fecdd52e6 | -5.86264 | -42.89702 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2de2a4ff-23b5-3765-a4ed-85d9e0239594 | -5.54671 | -42.64486 | 2025-08-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2d1d96e-3173-3a31-a7c5-e02baa3217d5 | -6.86514 | -44.3847 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6627616d-1561-38f4-b35b-da9327956b92 | -6.06287 | -43.43913 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06e6aa5f-d939-374a-97e1-db879237f6b3 | -5.76146 | -45.37216 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc0b0ed2-1445-3e3e-9381-18a0f67ae035 | -6.41507 | -45.60792 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b53d4cf2-f3d7-386b-8467-a800011183ff | -6.17246 | -44.20164 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f81d99d8-6039-3777-b05a-8241df66037c | -2.98153 | -48.60492 | 2025-08-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91ab08f5-14b1-338d-9eae-137a9bf42fab | -6.63631 | -44.39128 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e715bc-4e4c-3628-bbc6-d754601ed11e | -6.5622 | -43.68385 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a31e78d-593e-3972-920b-60d5698230a6 | -6.63677 | -55.27323 | 2025-08-30 04:19:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d60a6001-8f2e-3da8-9500-b33c851b3cbc | -7.09688 | -44.59909 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd14de18-86f2-37b4-86c2-055f3e45ccbc | -6.20001 | -44.00262 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a238bb1-7b21-390a-b57a-a42b481ac25e | -8.41054 | -47.35722 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788938c6-4239-3c06-ad4a-03a035631940 | -7.05964 | -44.8378 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77a7a509-d68d-3090-84dd-9d1f602bc85b | -6.6828 | -49.77437 | 2025-08-30 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f40d4bf4-c539-3731-9a1e-3b1f2eac7fde | -6.06428 | -44.95935 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a17d2246-8985-3c3d-b85d-fe8bf31ce8f8 | -6.80515 | -43.75745 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fefd08c4-5249-3adb-bde2-176fa155cfab | -3.7938 | -49.42892 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17e1f594-68e4-34f6-bce4-3fe1dff2d1a0 | -6.64459 | -44.25029 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b471901-ea34-3c53-9a09-8797cef38a45 | -6.17884 | -44.79358 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e23fac18-b03e-3681-8614-d79afb2ab760 | -7.66292 | -44.7879 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4ac1ec-5dd2-34ba-b286-4ddcd88105b0 | -6.17953 | -43.32133 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03fd5f6b-a962-3ccf-8636-dfe5ff4fecb3 | -6.88452 | -56.47291 | 2025-08-30 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c592518-3442-3c2f-b8fe-19a987ad9570 | -6.48565 | -44.39633 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df349d66-bdf4-3e6b-9502-d4365b708619 | -6.5384 | -44.58181 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6790629a-e84c-36cd-8d9d-26d7983e2314 | -6.15691 | -44.17072 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019b2bc7-86ff-3bac-9f73-afd753499024 | -6.53825 | -43.52695 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7ca1bb-e7a6-3ecb-b43f-6d3a1f9181c5 | -7.15787 | -44.14116 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 360f0cc5-524f-3cb5-ad9f-614b0b1b2830 | -7.94273 | -46.0173 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b36c119-1a9e-3f61-b07f-84e77d648ba9 | -7.11593 | -44.58788 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ee87b5e-88f1-3515-9ec3-f7df4c70f10e | -7.61107 | -44.72592 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28c625bd-ff25-38ee-be59-fc208d87df02 | -5.83059 | -46.35702 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69708be5-98b7-31a5-b868-54f860eeb59b | -7.80543 | -44.81025 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0617fdf-004b-3fc3-9f8a-50fd73ae8486 | -5.99923 | -44.72311 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc9d6490-8cab-3962-9bb7-9daf4069413c | -7.64391 | -42.65673 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9404df42-1aa4-3d5e-858b-e68aa4d99e7e | -7.71556 | -50.27637 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a904ed85-7ccd-389b-9d4c-60b37668f051 | -6.40165 | -45.58443 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68ac95a6-0c1c-3219-ae62-31579f2e0f35 | -7.72187 | -50.26776 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4767d538-d308-3c06-9e89-edc469d8335f | -5.87808 | -46.50277 | 2025-08-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| faf868f6-fbdc-3135-9a19-d6eaffba4c54 | -6.65848 | -43.94086 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cca44660-7820-3442-bf5a-59f9f89cf89e | -6.32631 | -42.52515 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f28239a1-1fba-3267-81f4-98c592f395a0 | -8.17966 | -45.05058 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ab6c6af-8310-3a0c-b343-c85c8ffbed5a | -5.44668 | -44.82273 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d19d3c-3514-3bb5-b093-2667ee6ab6d6 | -5.5976 | -46.23483 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c18cec16-bded-39dc-9c80-c86b85f96514 | -6.70282 | -43.09031 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5100316a-3298-3225-ae48-0fde80b17d2a | -6.65941 | -44.3735 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a2df81e-2516-3bf5-b1f0-531b941cffec | -7.71542 | -50.28115 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c3e0029a-e509-3946-85ef-b7bcadddb900 | -7.62879 | -42.66246 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 08b53ba6-7a34-3f11-a2af-6377b72f8ea8 | -5.82662 | -46.36013 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7c14290-56bb-3b18-8874-f169ef05e445 | -6.09108 | -44.00373 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e033628d-5546-3a77-9381-24093642fc75 | -7.16847 | -44.16068 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98b86752-57d2-3287-881e-4b0e4da16a87 | -7.10511 | -44.58974 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3b699868-6501-3b2a-9409-52ed840d2e5f | -5.69917 | -45.95694 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 584637aa-31f9-3d24-b24d-cb9f1178c402 | -6.56889 | -43.68491 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bc62601-85ed-3a8a-99b0-c80153f63b2e | -6.24284 | -42.40663 | 2025-08-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 67c29d31-4c46-316d-b665-6da26cd92dee | -8.11415 | -45.01181 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3097e641-480c-3334-8acd-d9377a3ebfdf | -6.30836 | -44.42206 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb905ba8-9347-34dd-b752-210b01f53cf8 | -7.74252 | -50.26834 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16005780-d309-3240-8d39-9afbfab7b491 | -6.41395 | -45.59348 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b60d2472-dc35-3795-ba8a-94ee823bba7a | -6.89717 | -44.39684 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98a19a45-8a1d-3a75-bccb-79b44cb1c167 | -8.38235 | -44.70895 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c57897e3-67ee-3407-9d77-46f21464f7c5 | -7.1572 | -44.90969 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53be2d57-e6a6-36e7-8719-150376e22f6c | -6.52117 | -44.86548 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e2f07474-8570-3d24-a173-23457e610d0b | -6.32977 | -42.52572 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b12769e4-ce5b-3f14-a55d-aeff78e08737 | -6.31274 | -44.41563 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a10b94c8-9d19-39cf-8cd6-5f70dca24dc5 | -6.50188 | -43.54728 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abdf6220-47f6-37d9-a9e1-2fc99844cf77 | -6.94865 | -44.06517 | 2025-08-30 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efe9cc3b-127d-32da-8470-9ebef5221e14 | -7.06154 | -44.28012 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2135c1e-6bfc-3b66-beac-3942b77a0ab7 | -5.82892 | -43.85177 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3985e0a4-3121-33d7-8491-5295acbb08a6 | -7.9595 | -46.38198 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d0c687c-a3eb-3a0d-8f8d-b7b530ac0df4 | -8.24265 | -47.19999 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 112026e8-fd92-3d5d-a6b3-bcfe7a13b89c | -6.17168 | -43.32754 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08565a59-cd13-3221-a289-02332e918baa | -6.48789 | -43.52665 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f901d74-3adb-31c7-864a-1dd18f04e358 | -7.11403 | -44.44538 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0bdfbf9-b8c9-3e6e-abcd-739c0aa1c53e | -7.16901 | -44.15719 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed5cbba7-eb6a-3426-b247-6995cf69248a | -5.74379 | -45.37651 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f618d20-fe55-3aa5-bfae-8eb25b566e71 | -6.54215 | -43.52388 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d2f302-0621-3bcc-b51c-ff3baffac854 | -5.8318 | -44.83765 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 652d6064-a461-349a-8e63-ceb39d70dc0e | -5.59053 | -46.32283 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e107c41c-8230-3a02-a23e-fca82f47ec67 | -6.77722 | -43.78899 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d4034a4-9a3d-38e5-9729-f2a1788a8489 | -8.34404 | -47.42003 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbfd4b7d-03f6-3803-9ba7-1a3627451a79 | -7.78023 | -45.47315 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 222d7ac4-2334-3a81-aa29-ba15515f11d6 | -7.22549 | -45.45262 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c98dc27f-3bc6-3c86-b70e-fa9286d8ff87 | -7.63984 | -42.66012 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ea4bbd43-f0bd-33b2-b993-7e6de4e669eb | -7.58538 | -42.70375 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
