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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c79875dd-245f-3856-b88c-937e8201aae5 | -7.84534 | -37.05875 | 2026-06-25 04:14:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b895918c-199b-3739-8732-8be875b65d14 | -4.663 | -43.22184 | 2026-06-25 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a2c21b8-68e3-38a8-bd96-405f1212a8f4 | -7.72651 | -44.56124 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56723676-5cf3-3741-8937-9ac9d5f7abb6 | -9.20472 | -45.32206 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39b69578-e489-3bd3-acdd-b7209c943e88 | -5.78795 | -45.04576 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a73987e-deba-351e-8b26-20acde6f29ba | -9.21429 | -45.32738 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b12b8a2a-36c8-3784-b85b-4bc183172786 | -7.74388 | -44.6189 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 51bf2843-9a7b-39fd-8dcb-bb64c4eceec8 | -7.75001 | -44.62353 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd43761c-cad8-398c-a8a9-8fa387eaaa97 | -6.99998 | -42.77174 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 477c2c0c-e413-354a-aa29-9838ff90c546 | -6.99216 | -42.88718 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94d7b23f-5e03-31cb-a6ad-3b8bdde075e0 | -5.80909 | -45.06859 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3be4ca-c5fb-329e-8b68-68d1e501eef8 | -7.74445 | -44.61532 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1a2329b-489c-3a65-be45-1f987a71a50a | -6.76141 | -46.30789 | 2026-06-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30522e43-31a0-3d70-9eef-2600e8c94736 | -8.79596 | -44.80999 | 2026-06-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd8334c8-cfed-32df-886f-f4b18745313a | -9.57508 | -49.12191 | 2026-06-25 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caae014f-c7eb-33bf-b496-7ebc9fd15d9d | -7.73926 | -44.17846 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b40538-36e8-36c7-92e9-44a00bc3af63 | -7.75115 | -44.61639 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fb7a95f-bce7-3f23-8f9b-aecb92795543 | -7.63238 | -50.21137 | 2026-06-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0fef232-9a4c-3735-9e8e-62b9e09d558f | -8.67987 | -47.85674 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d023f117-bede-3417-acc8-8423feb5843b | -5.81024 | -45.05659 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 719f4033-f7f5-3b3b-a78e-523f2f69fbbc | -6.99055 | -42.89753 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 39d68bb4-9491-38e2-a0d7-8d947cb406ef | -5.81089 | -45.05721 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aeab45f-5491-3bdc-a756-82701ba4e141 | -8.85954 | -46.93282 | 2026-06-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c7743c-33b0-3445-97f7-8b300bfc3d6d | -7.74167 | -44.61123 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cb03110-ac0a-3a54-8307-8626f81a0bac | -7.74551 | -44.63016 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87c5750a-2917-30f6-9753-ed76be5ccd1a | -6.97844 | -42.88858 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| feee2767-609e-38c4-80ac-09bbac1040e6 | -10.02953 | -46.61604 | 2026-06-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39d27831-3935-3d01-9da4-3dc0eb340c49 | -7.73262 | -44.1774 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27035a62-a926-39f8-b8a8-d1b23e415c41 | -6.98725 | -42.89702 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 3acec028-3666-3606-bfc0-32901116e98d | -10.29597 | -44.692 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4371950-137e-3c7f-a02b-a966a0215334 | -5.82313 | -43.59404 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11e798b9-a0dd-32ad-b02c-5ff5ebabf7e9 | -6.99944 | -42.7752 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7fed3d8-d94d-30f0-8938-ffa86ee19dba | -5.80804 | -45.05288 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f7f03b1-1e2b-37ff-83e6-28f7dd59c01f | -6.90578 | -43.68055 | 2026-06-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90b732ec-cd4d-387e-8073-5a694dae14ad | -7.18818 | -42.91834 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ec2cc37-4641-3fb1-99e2-d1ba468df45e | -9.11029 | -47.46558 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7692a3c-1d40-39ad-9d28-0e44ca2a47a1 | -5.80963 | -45.06037 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76604676-4057-336a-b67d-784ac1dd5002 | -9.5333 | -47.7536 | 2026-06-25 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c895d875-66b2-3efc-8017-973565eb7dca | -9.36888 | -50.54494 | 2026-06-25 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86b414fd-4147-3aaa-bd49-22a227ec62a9 | -9.09681 | -47.5242 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4df85825-88b8-3ac9-bb94-25aa467020d5 | -7.75394 | -44.62048 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 36db1273-857b-33c0-be12-df1b165b446c | -9.2109 | -45.32682 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f98f4e28-e7ae-387c-87c2-295e00c98f9f | -5.8084 | -45.06794 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b13eca67-e924-3e70-bb23-1cea2af18316 | -6.90964 | -43.6776 | 2026-06-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d6676fb-1f11-3e59-86e4-a9ffe293699b | -9.36971 | -50.5403 | 2026-06-25 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d5306dd-7fd0-3391-8e9e-4c09522a27b6 | -5.81246 | -45.06473 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcd6a9b1-adc0-3198-9b1a-15770a0135df | -9.5792 | -49.12259 | 2026-06-25 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d88f700-6fad-33b0-94c7-a2b4feda2a76 | -5.81148 | -45.05343 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa629d8c-e1d1-348b-8ca8-338877785af7 | -9.2813 | -47.65505 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d86bf6d-a2f1-39e2-8c3c-b878e9d228c4 | -5.80969 | -45.06479 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e93e293c-f47e-3228-885d-d23ff77696d5 | -8.12587 | -47.89169 | 2026-06-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51373b9-53c1-327f-a2eb-0459e350aa99 | -5.90462 | -43.85454 | 2026-06-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37ce213b-19fe-3bef-8b54-d57423156abc | -5.82036 | -43.59003 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a69e2d5a-6986-3330-8e2c-c1960d74b1dd | -9.16112 | -45.39817 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1e80f0-40f3-3c4b-b509-2ebf4e7cbf0f | -5.81029 | -45.06099 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7be8a75f-a7d4-3230-921b-9dda2cda5409 | -5.78856 | -45.04197 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0362a5b1-fbe5-3bd4-ad5b-5721b616e083 | -9.36434 | -50.54418 | 2026-06-25 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52b1680b-4a7a-3ab1-8565-7426186daa62 | -9.19795 | -45.32095 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7a86749-d999-378a-981a-42ecb95fe7c7 | -5.81208 | -45.04968 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a82104a6-537f-3726-8925-051135e6332d | -6.31107 | -44.64722 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f98497df-0004-3a24-9e09-9cd0bbd28a1d | -5.81207 | -45.04531 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1160d9-04f6-3ebe-b0a1-a6f742e14e89 | -9.91249 | -37.09278 | 2026-06-25 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08ece302-128d-3518-a2eb-924404a77c25 | -8.85588 | -46.93237 | 2026-06-25 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d850fb8c-70e2-353f-84b6-779255690d5c | -5.81562 | -43.79316 | 2026-06-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 406cd57e-eba3-310f-bc17-6099c1ddc271 | -5.80902 | -45.06415 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20b064a6-7e1b-3d71-a8a9-9cd4f71d681b | -9.14219 | -47.97977 | 2026-06-25 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b9b228a-0892-30e8-bb8e-7a15ea2994f2 | -6.9746 | -42.89152 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c7692d01-ee0c-3ee5-ac00-c751c5f03266 | -9.98729 | -47.73781 | 2026-06-25 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e272596-52b3-3371-8a24-7d157356eede | -6.87014 | -43.66761 | 2026-06-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f39d6315-8d81-3374-a51b-abd66886cd78 | -6.50339 | -42.22248 | 2026-06-25 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64763392-14a7-32f5-b3c2-779ae7f9d04c | -8.85515 | -46.93677 | 2026-06-25 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61efd956-f731-33a5-ab1b-650cd7549aa4 | -7.72598 | -44.17635 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5c6b14b-54b2-3fd0-b6fc-3fa519f19826 | -5.82367 | -43.59055 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79fcfcdc-3b7d-3988-a83c-2ea4ca0245e7 | -7.74109 | -44.61481 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1cfb140a-9c4e-3fef-ab0d-34b7cef9bcb5 | -8.0661 | -46.38831 | 2026-06-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1b07d25-eecc-3afd-a4cb-d16d43ba893e | -5.81617 | -43.78965 | 2026-06-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05171c06-aa42-3649-ae4f-deac59ec7738 | -9.14138 | -47.98465 | 2026-06-25 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e2665a1-22aa-3f38-8d13-228ad59bc3aa | -7.63694 | -50.21218 | 2026-06-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 222e312b-a725-3cb5-9169-4bdeb45a6a9c | -6.99722 | -42.76778 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 68707833-bed9-373a-af10-fd138f8a0b38 | -9.74673 | -45.3385 | 2026-06-25 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a462333-7058-3a28-a181-fe5ef4ce6424 | -9.98353 | -47.73725 | 2026-06-25 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e70a226-0b6d-375e-95dc-00ce1a9bf7ef | -7.74837 | -44.61229 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0f4b08d-a72d-3246-b4b6-87a0ba1ba281 | -6.99775 | -42.76433 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46c114dc-1fcb-315e-a1d7-9ac52a7d5a9c | -6.37355 | -37.37704 | 2026-06-25 04:14:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6bab7616-49de-33e0-b310-383bbe9c1f64 | -7.74608 | -44.62658 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f01d653-bbe0-3394-9433-41e53c9c018f | -4.66354 | -43.21838 | 2026-06-25 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c8a99bd-ed6a-3bbc-972a-9bde24e299ed | -7.00221 | -42.77916 | 2026-06-25 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3573aa9-4aa1-3631-9a04-ecd0a26081b9 | -5.90406 | -43.85804 | 2026-06-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8c5aedc-e171-3daa-b45d-dea301c707b9 | -9.36517 | -50.53953 | 2026-06-25 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3fc6bf7-a74f-3749-b0dc-f0ceb4b45528 | -7.80736 | -46.45832 | 2026-06-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16c1f173-590c-376d-a007-c43513bccce6 | -5.75379 | -43.18946 | 2026-06-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fcbd5b71-af98-336f-9906-ab9a5fb31895 | -5.51017 | -35.59893 | 2026-06-25 04:14:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e000d2c8-4a67-308c-9517-59e9e8e5bca4 | -6.3105 | -44.65086 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94741f1a-cd78-3e14-ac26-2247434f72cb | -5.0478 | -43.2654 | 2026-06-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c511a551-9078-340f-b656-d2f872a3359e | -6.97407 | -42.89497 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edd5ba02-6079-3fb0-b3c5-00f2b18c6563 | -6.31119 | -44.65452 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9e87a45-280b-3c21-8100-d432f4e6fc68 | -7.73594 | -44.17793 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a49fa743-2c60-3ed4-8574-391e9e5aed31 | -8.12976 | -47.89231 | 2026-06-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81ca7f43-a048-3255-bee0-3eb982d99c58 | -6.9779 | -42.89203 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac064eda-df98-38bc-98e3-6e032740dfb3 | -7.75786 | -44.61744 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README8.md)
