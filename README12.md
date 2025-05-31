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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6315761-ee3e-3941-97fa-256dd19f2499 | -7.58617 | -45.86303 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51190224-d1fb-3bc7-a63c-8bf81119e72e | -6.34213 | -43.38268 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c233cc-7055-385e-bbcf-6595e32fb670 | -7.00679 | -44.61314 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3e1e391-c80d-30c4-8e55-ac8b39d60bda | -3.28268 | -54.91145 | 2025-05-31 04:51:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1dcb707-704d-3d68-b392-693aac7de893 | -6.2226 | -43.34631 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69bb2b08-53d2-39b1-9002-bb6b482a965f | -7.00598 | -44.61886 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd3588ed-97a2-3994-82a9-8638ea846150 | -5.82941 | -44.0843 | 2025-05-31 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8478f01-7272-325e-91b5-6e796887b59d | -7.58344 | -45.86538 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d9931291-b074-368b-9861-cd2c00e77fbc | -6.22311 | -43.34276 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dca2eb9-bd5c-3982-b04d-78cb604929a5 | -5.85425 | -43.64176 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a2c9e4-7893-36c5-9f37-9872051c6a1e | -7.58279 | -45.87014 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15ad6fcd-cc50-3475-a8d4-f9d666730cba | -5.0528 | -43.24511 | 2025-05-31 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a7ebfdb-9ea4-349d-a5e0-8b24d0b11a00 | -6.54656 | -47.80882 | 2025-05-31 04:51:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c942ce6-8e64-3047-b2b2-6b6bd25ba5fc | -7.01175 | -44.61435 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b38f28e7-91e5-3aa9-918e-bee56d04ea3a | -7.58015 | -45.87186 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d06ba9f-f21d-3a29-ae94-e2116e613513 | -6.2177 | -43.34188 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db68e1d3-cbe4-3a80-bbb1-64afca3d27f6 | -7.00682 | -44.60808 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37e22f72-8794-3a78-af2f-5878a2356d92 | -7.75102 | -46.56801 | 2025-05-31 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa907087-6677-3abc-aad0-1ba17db75569 | -7.30916 | -49.57466 | 2025-05-31 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cfd38c4-38b6-3fb7-ae1d-d38b2cef1c3c | -6.55627 | -44.48687 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c64163e-32a9-3d22-8418-407792abc255 | -6.27657 | -44.20195 | 2025-05-31 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b40d6764-e28a-3e05-9c17-4d5f1bb803d8 | -5.83372 | -44.09092 | 2025-05-31 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aefdd5f-4fd4-3874-9776-25ecff1acc0c | -6.33672 | -43.3818 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e87b2efe-a421-38f9-886b-2882289e1736 | -7.01093 | -44.62007 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3118faab-00c7-315f-99c5-47dce667f5f3 | -7.24894 | -43.09118 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3ae7ffe-1fc6-3896-8bd8-db7de71712a8 | -5.83413 | -44.08795 | 2025-05-31 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a7f2844-ba1e-3d5b-8cd2-a4fc310922e6 | -7.58548 | -45.86779 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f048b7ad-fe57-3e16-a414-e0eae57fb40b | -6.34019 | -43.38275 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00e807b6-9fe1-3d1b-a035-ad00fc073ba9 | -7.24844 | -43.09488 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca3de706-dd36-3b53-a9ef-a76689556268 | -2.90611 | -54.48961 | 2025-05-31 04:51:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b7d1ee-bd99-3dda-bafc-3c5131291e55 | -7.08369 | -46.0495 | 2025-05-31 04:51:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f70acd8-8448-3927-9919-d1b80912512f | -6.20293 | -43.32903 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfe1b430-7362-3008-86e7-59141564f1a8 | -7.01024 | -44.62071 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a867af00-8fae-361a-9987-b1591a0d2081 | -7.58153 | -45.86232 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f08b6e0-3aa4-3d3a-acb9-78e2fb5a9d8c | -5.84897 | -43.64096 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3543ef4-d8b7-338d-9902-693c5d13a5e7 | -7.43105 | -45.4198 | 2025-05-31 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24a112e1-82d5-32bd-9ff3-355da0755ed2 | -7.54383 | -43.30802 | 2025-05-31 04:51:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b2db377-3359-378e-b1a5-b5ac70313d02 | -3.71025 | -53.70974 | 2025-05-31 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39177814-7aa6-3d9e-982c-4bbfab116266 | -6.15592 | -42.61641 | 2025-05-31 04:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 534f966e-41ac-3676-b9e2-841db2ccfee6 | -6.56134 | -44.48739 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 933faf67-c7eb-3d48-9c18-d395e3071d35 | -6.21279 | -43.33755 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c91152a8-717b-3642-8366-5902667a51fc | -6.82826 | -44.65219 | 2025-05-31 04:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 150a2316-7fde-34cb-bb65-f315fc313bec | -7.01011 | -44.62583 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ffbdba1f-b8d8-34cf-92db-2bf1f3f0add0 | -6.21327 | -43.33417 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 606b85c0-acc7-308b-add3-d9a41ebfc299 | -6.20691 | -43.34 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33edbb0d-1b68-35ec-a3ac-260b1d6f114c | -5.829 | -44.08729 | 2025-05-31 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5c9a4fe-7570-3c36-a723-a8278028c584 | -6.15073 | -42.61196 | 2025-05-31 04:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 08ec87fc-d61f-3930-9c9a-ec920726ed0f | -6.33478 | -43.3819 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dba90f3-a7ef-39c8-98f0-83220caee601 | -7.58084 | -45.86709 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2dadcdd-47df-3be9-bff4-9b1105c1873f | -7.00605 | -44.61374 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d44d077-3ed1-321b-bbe6-db79d1faa218 | -3.70684 | -53.70919 | 2025-05-31 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ff4d224-14b9-31de-a090-8521678b2623 | -6.34559 | -43.38362 | 2025-05-31 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebce1265-f3b8-3817-b9a5-ed054bf41af6 | -6.54708 | -47.80534 | 2025-05-31 04:51:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63857f47-8b6f-375b-a1a9-982f9ca8f76a | -7.08434 | -46.0449 | 2025-05-31 04:51:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f2abc5a-cef5-3456-a1cb-b8d744c2e5df | -5.86282 | -42.84324 | 2025-05-31 04:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e751775-cbab-3040-8954-a5a709f0e6d9 | -6.15126 | -42.60814 | 2025-05-31 04:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 84d13307-4a23-3fa2-ad7a-ff166700c81d | -5.85724 | -42.84246 | 2025-05-31 04:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3288549-6394-3e46-878c-bca11e98b186 | -7.24286 | -43.09404 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 378eee22-bfdd-3fd9-bd62-b3b461bdaa87 | -4.81846 | -44.35686 | 2025-05-31 04:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 587ca3d4-4806-38ba-934e-c7f2c80ac801 | -5.85471 | -43.63858 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 345f7786-ad03-3685-80fa-853077e5120f | -7.57619 | -45.8664 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5727ad9-8ad6-3d12-aca5-fa08d0293f10 | -6.15644 | -42.61263 | 2025-05-31 04:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2e5e86df-02c3-3ec3-9f17-b9d2d1eaf214 | -6.27143 | -44.20137 | 2025-05-31 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6245ac9a-0656-3a03-8f98-f55635634ff8 | -5.85775 | -42.83889 | 2025-05-31 04:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ece3427-a129-3f0a-a0ba-a5cf03be4e37 | -7.5848 | -45.87256 | 2025-05-31 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64563d7c-1988-3f2e-bb35-652f64b4f27d | -13.10325 | -45.28764 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 954b1572-8ab7-3ae5-b268-98750b3df46e | -10.6174 | -44.76686 | 2025-05-31 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcea25fa-8328-3f47-bbc9-8d31ff911ec8 | -10.46699 | -47.94617 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e34bdc18-385e-3f69-bf80-f78c9932cc4e | -7.30796 | -55.30918 | 2025-05-31 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db9d997-ce4b-3b88-99a4-0dde6f6b3e88 | -12.03729 | -54.96422 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bef186c0-6bcf-39b9-8863-22f4abc2c9ae | -7.9909 | -50.68497 | 2025-05-31 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a4ad321-e3f8-3f86-a86d-d74bccfec6e9 | -12.03671 | -54.96783 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8e19107-f181-3d65-bd8b-daafa058fdde | -11.30967 | -46.47908 | 2025-05-31 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 632c4bb1-a746-3196-9148-2348e918eacc | -7.95306 | -46.16249 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88028a5a-7bf1-33df-80a6-c7ab3a92869f | -13.10364 | -45.28437 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54430283-c348-39b8-9439-7d522fab2daf | -10.82771 | -56.94857 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da047214-75c7-35e6-954c-73bbcb81d202 | -10.63902 | -49.43039 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c43145e2-3f57-398b-b4dd-befae2eca3e1 | -9.91989 | -59.90775 | 2025-05-31 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 933a5c55-50b7-3cfe-b09e-3e27b814e65d | -11.79393 | -44.28299 | 2025-05-31 04:53:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5825bd8a-ed9f-33b4-bee4-e336f66fb8d2 | -11.91389 | -54.82169 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75d00263-7ffc-3614-9f32-cf4f3707050b | -10.68989 | -57.65193 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b1f8833-19e3-30c3-b859-3af59f862350 | -9.39618 | -48.41671 | 2025-05-31 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62f25f6-2fd8-315a-98c3-1e667ae65a63 | -11.3607 | -55.13155 | 2025-05-31 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c20be1af-7365-36a4-b766-cc71795d9ffb | -11.04057 | -53.99852 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d60ed332-c745-3aa2-8bb3-9af78c53e594 | -11.64332 | -55.3699 | 2025-05-31 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938d4373-1b4d-3386-925a-8455d99a3a34 | -9.24425 | -51.22598 | 2025-05-31 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 958b4cdb-6554-3799-9306-dae45d040870 | -12.02048 | -49.51651 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2184a95-1061-3cd9-b62f-4b49dff3c6b0 | -10.47059 | -51.8928 | 2025-05-31 04:53:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 062aedfc-8769-3dac-96b5-c7a96d067e1b | -12.01521 | -49.52589 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 69d8e9a2-e390-31c0-a05f-8516ab046997 | -10.64285 | -49.431 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4b3a3f9-cfe7-368d-bbde-808977bb0de6 | -10.65437 | -49.43277 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 507f580a-ae7d-32e6-a887-fe46d6d0a0b9 | -11.14037 | -53.94278 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e127904f-0247-3b5b-9f4e-135b35522dc0 | -12.01853 | -49.52982 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 27681667-a99f-355e-a6a2-384aba8727bc | -12.10453 | -54.66247 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3a72d22-ab67-3e91-8a8b-15eb44f99fca | -11.90661 | -54.82417 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a3ff29a-3ca3-3050-b8c7-9de1c7177bb5 | -8.09375 | -46.28649 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9eee8c3-1535-38fc-a0b9-a571fac90f2c | -9.52952 | -54.76985 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea968fad-401a-3857-9a52-c6e98d01979f | -12.10672 | -54.67015 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 298534e2-d1ba-3217-8847-6ebf364e2a33 | -9.51614 | -54.74527 | 2025-05-31 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a420453-936f-3838-afda-64cd15cfe343 | -12.18424 | -54.24963 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README13.md)
