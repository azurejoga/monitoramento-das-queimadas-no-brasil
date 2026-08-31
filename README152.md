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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b533b610-4865-31b3-a989-1a9b7dde00b9 | -5.3449 | -45.16257 | 2026-08-31 16:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e72a1b1d-ea1a-3ed7-a61a-b59003a43a6e | -8.50386 | -55.31557 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 9f2c7843-accd-3d52-9eca-3d0f30a45fad | -10.11392 | -45.84433 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 59cb6345-9163-3488-afae-42b996013642 | -13.62678 | -51.83683 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4762ec5a-0244-39ef-a6ad-3da94a26447e | -10.15217 | -45.76986 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 68afa07a-89d2-3724-aac8-ac54bc85666d | -8.15232 | -45.46394 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 68efb926-f438-3595-8207-dc8bcf130a2c | -13.97027 | -54.41626 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b0026153-d604-3c68-b46b-1feb11d32648 | -5.58786 | -42.33187 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 63199a61-12a5-3656-938d-22a3b6da781a | -9.98416 | -53.92948 | 2026-08-31 16:50:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 9ef222c6-4bb2-30d5-90a6-f3911a3025f2 | -11.20714 | -45.05447 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2d2735a9-16e8-3b98-98da-8ed5cfdce244 | -8.76972 | -46.44905 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6aa7b03c-8ad4-37fb-9862-dfbc56054840 | -7.9995 | -44.28119 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 481eb769-1a6b-324b-a2b9-9551f9376388 | -10.85578 | -48.35122 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5dd3c07f-1592-36ff-8aee-dd0324855448 | -7.92138 | -44.29686 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04e49fae-b28a-391b-bdca-697696eb45e6 | -10.55833 | -46.16763 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d5a1b6f9-801a-3f98-b41c-bd5b911ac9c1 | -7.43457 | -44.9465 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f02950b8-99e0-30a2-8dc0-1b763512075b | -13.84057 | -54.09658 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d4ac89b9-93f9-3561-908a-efb497955a6f | -12.17125 | -50.52522 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bca59eb8-76a7-381f-9243-af4992a0cc40 | -11.51533 | -46.94678 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e620ec47-02f8-37e6-8a96-204ea2660e58 | -8.88281 | -46.03031 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 86b7b8f5-ded2-353e-aa0e-4ae25daf7e56 | -11.71466 | -47.64363 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e2524535-7412-3d0a-b10e-01fbbc578c6a | -12.96277 | -45.94294 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 45012ea4-a8d0-37db-ad2c-d1345fc837ee | -7.45668 | -59.93737 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 7b0559e2-ed81-3af0-81b5-42a8c4f9c33a | -10.02507 | -45.56235 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4f29c876-45ba-3b50-9cd8-84a399334496 | -11.23538 | -45.13844 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 68e8ed51-8f17-3ec6-868a-593f4f75f472 | -9.68261 | -47.93547 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 06485135-5cf1-3ddd-803d-5f435a88fdd9 | -6.91771 | -52.83377 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba09859f-7d7f-361e-8692-cfa96669d94b | -11.87649 | -45.8146 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 03115ebd-507f-3262-8f68-8cbc29a41444 | -7.77805 | -44.06026 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 690c7a4d-e31f-3ff5-8289-ace758f92466 | -12.09465 | -44.98635 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 28928f38-31e5-359e-a1b0-52cbc9bc3872 | -7.77006 | -44.06104 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e8738fe-1b91-3d88-a122-b01e16d2d5b6 | -7.64429 | -46.73316 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4fcbbeef-d3fb-3eff-a5dc-79fa9218ca09 | -10.78815 | -41.32246 | 2026-08-31 16:50:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4dbafe30-a8ca-3229-b256-6643eddc4b56 | -8.39503 | -44.99133 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2df5959f-0f6b-31a8-90e9-755e2f16be65 | -11.54399 | -45.47607 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 35f3e3ba-eff0-39cd-9647-ec5a8bb1fb36 | -7.04573 | -45.40245 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4238d613-d733-3f25-b460-9572c3d731a3 | -7.09495 | -47.42882 | 2026-08-31 16:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a95d04f-cfdf-3411-9cc0-765999e3f002 | -10.68486 | -46.27764 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 949e4294-d0b4-34e4-a199-7e0672286497 | -11.25255 | -45.11517 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f8d86f8b-dbf1-3641-afe5-a21e560061fc | -9.16081 | -59.54746 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 505988a3-0721-3b9b-ac57-86a9ef0b44ea | -8.49395 | -45.53138 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 822a52da-b274-3b6f-878d-a1175895c335 | -6.81656 | -43.54394 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c041945d-8c67-34e5-b8ea-2eb19b1b5391 | -10.18086 | -42.22074 | 2026-08-31 16:50:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2788be87-074d-3b9b-ace0-850c90c3dbcb | -10.99004 | -48.38711 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1d3e36ed-009e-3cd7-9300-aa7ec24e5737 | -10.98726 | -48.39113 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d03e54b4-30f8-3b96-babf-cd015b97d210 | -6.60884 | -48.6941 | 2026-08-31 16:50:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f89bcdf-cd68-3f2e-867c-3b62be13af15 | -11.24549 | -51.24431 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c44c6cde-76e5-3a58-a86c-7f4104442ce8 | -9.16025 | -59.54296 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c60aa8c2-a5b4-36bb-8439-4c6b4d5bfa62 | -10.06456 | -48.70384 | 2026-08-31 16:50:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ec9bafcf-b76a-3917-a6ca-a45ed97e1233 | -11.54528 | -45.48397 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e7e65a43-7465-3727-b89f-51ba34f2a1aa | -7.9909 | -44.27747 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| e880c7c7-ce1f-3883-aa18-0c67e06b188c | -10.4099 | -45.08021 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f43f498d-bb86-3a65-b82f-afde79a020f8 | -9.42292 | -56.97916 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e78a9600-ebea-3f0c-88dc-b58b0decdc1b | -7.1718 | -44.68575 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cac61e29-0cde-36e5-add3-ae6cdcd0edc8 | -13.42279 | -51.38706 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| abb78938-f9b7-3c96-8de2-e9ee39ae5850 | -11.51199 | -46.9473 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ccf87a0c-444d-31fd-943d-0c440385acc7 | -11.31925 | -45.18819 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4757ea9f-cf60-3250-b295-2eef07f98387 | -11.25324 | -45.11932 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 532907f7-9728-3743-8ff4-5e97d8fb54d2 | -6.93475 | -55.63816 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7ee6325-7854-3082-a0c6-286f1fb265d5 | -11.48724 | -58.51702 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f48b7a5a-4603-3485-b257-ea2ab6ecef80 | -10.73592 | -47.96511 | 2026-08-31 16:50:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fc8bed5e-fb2f-3bf6-a348-cba39c4aa4ed | -13.30499 | -51.59818 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6750ddab-3f90-3c70-ae88-c60299efe099 | -12.07454 | -47.20454 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c8719f4d-f23b-3c71-9ba4-37b1919fd13b | -9.14318 | -49.90553 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5744c5ad-bc0a-3617-9ec2-6524a9e3e539 | -11.21759 | -46.1017 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9eeddd16-6a9d-3ee6-9f2b-7b7305ed93b2 | -11.24831 | -45.12805 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9ed65c53-9f57-3e7d-a1c4-d4d6fe78fb99 | -7.605 | -44.9949 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c272ecd-93de-303f-9673-d47288040ece | -9.68315 | -47.93897 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4b6fb217-c340-3bb1-835e-8eb69b8f1e98 | -7.29738 | -56.69092 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c7f92fb4-8ef3-3738-8c07-354ed1859a7c | -9.48644 | -57.02713 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a642e9be-b313-34de-8ca0-d6045ce9e247 | -7.98784 | -44.28305 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ab7b26a2-2d60-3d30-868f-4dae0e064ffb | -11.84262 | -41.50938 | 2026-08-31 16:50:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c79909fb-49de-3ee3-8b32-189537a2672a | -6.76508 | -52.90454 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9736bb1c-3e29-3e84-85db-1c69103a3f40 | -13.96844 | -54.40182 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7febcfa9-9fe6-3a01-8a6a-0a37659dd9ff | -9.67685 | -48.31917 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7738a6ec-c70e-3d6e-99d4-87279f5fd946 | -9.43258 | -45.6404 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2c809c7-03cd-34e5-adc0-401735046e21 | -6.87492 | -43.71846 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 327a88c0-3c8a-384e-8367-e46fcf65b89d | -10.10827 | -50.30595 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f00f81b6-4710-338e-bf3e-04062a97b618 | -13.83611 | -54.09724 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ae5058d2-0611-37c6-8346-23e3ffb58a6b | -8.21069 | -54.94722 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06201273-f23d-30ff-a232-089b02adbbdb | -8.76604 | -45.39007 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| a52b9419-6483-3a01-902c-c74440dadf77 | -11.2479 | -45.10279 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 499424a1-d71e-360c-90b3-c666035d386c | -7.3651 | -45.06799 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bad52bd8-c65b-3cdc-b8df-2ec3b3860f50 | -10.02089 | -45.55888 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1dd2bde5-c986-3f53-9054-874c072f5176 | -7.55843 | -57.73258 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be118b5e-cbdf-3b7a-8457-cf3307d7c135 | -8.86325 | -47.08082 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 783bb018-0873-3f2c-8407-ae105f1e9580 | -11.20289 | -46.11936 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 68dcd249-723d-3018-834c-ebae92e63f73 | -6.61215 | -48.69359 | 2026-08-31 16:50:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 340dc253-fda2-32aa-9c92-e5fc2b016388 | -9.20445 | -51.5662 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3efbd743-bf55-3bd1-a717-c93c5f776ea1 | -11.67176 | -47.60727 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6323842b-3468-399b-9fab-c5c29ebc3b18 | -7.63964 | -46.72613 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae6dbb38-f0a9-3c35-8856-d9b79a8f52ab | -7.58166 | -61.33737 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2df6264a-6ce2-3091-921c-cd357173b162 | -13.43005 | -51.69316 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d05a4023-5a3b-3edf-af4c-dcb4e420eacd | -7.55037 | -60.47249 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| a8f7a200-1e09-39e5-a15a-27e84a1be66d | -13.05996 | -52.73299 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2b4e4f46-4bbf-3c96-b9a4-2fd41cbd77c3 | -9.20332 | -51.57135 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f6eebc44-b37d-30ed-a04f-2ff8d5a7ec4e | -9.44732 | -60.52543 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5fdadff8-0840-3a2c-b411-5a7f426cd632 | -7.05241 | -45.39685 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8147a1c7-856d-3eb1-bf76-a93194731eae | -6.80664 | -43.56117 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f342269c-e1de-320f-9f23-c848c6e9d602 | -5.57898 | -42.33192 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |


[Clique aqui para ver as próximas entradas](README153.md)
