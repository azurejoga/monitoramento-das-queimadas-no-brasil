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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 084024ad-b2b3-31b4-95c1-452e40f0ea57 | -1.55716 | -55.88614 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a0113b-6f3d-3b94-8fa3-76ef96ce45c7 | -1.51733 | -55.68494 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c59439b-d5fa-394a-a338-ef01db438b89 | -1.51678 | -55.68855 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65deb07c-e97e-366b-8d8a-35821bd0c37c | -1.41869 | -55.48458 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2250e327-1d3e-3f32-8cff-d13009f0b091 | -1.41808 | -55.48175 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13ed6eaf-4f9f-3ed1-9bd5-c1d908f85605 | -1.33828 | -55.44685 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee48d00a-6956-3397-9991-4fc9d2037b70 | -1.26019 | -55.68834 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 55f6a962-1122-3f19-b830-e4a87f61aab5 | -1.25963 | -55.6919 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 71dcc001-3799-3596-860f-b668ff0cd2b0 | -1.85272 | -55.1562 | 2024-11-02 05:27:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e28857b0-2e53-34d6-a829-3b897bf0a431 | -1.8038 | -55.16105 | 2024-11-02 05:27:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059fdfbc-aa1a-3992-9e1f-96c3a3e75e62 | -2.34304 | -56.50591 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba92cf4-75b8-37ae-9636-ea2724eceada | -2.34068 | -56.4953 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5acc3539-e7dc-3bc6-94b6-ca9d4ca517a9 | -2.33566 | -56.46528 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88e6540b-44af-3ee6-b94b-5dd84e570951 | -4.65677 | -55.91112 | 2024-11-02 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3791a653-b59d-3e7e-b3f2-8a49e6b428d9 | -4.25621 | -55.50788 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a436cbe3-0479-3172-9889-8c2456b60f14 | -3.72497 | -55.55478 | 2024-11-02 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc1dc744-7bc6-38b8-8c4c-328dfa5a222d | -3.70172 | -55.56369 | 2024-11-02 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8143e0-5c51-3f94-9324-3cbdaf424076 | -1.05929 | -57.40628 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1962f3f8-67bb-38dd-bb7d-70f993573938 | -2.58627 | -56.99188 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4758a4f-a7c6-3612-9736-bced90d8b889 | -2.58553 | -56.9966 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce992782-5dd0-32f1-9e5e-018309bfd111 | -2.58492 | -56.98898 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6995acc-7d5e-3b70-89aa-15768ef45025 | -2.58436 | -57.07065 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a5470b-2414-3a06-89ef-1bd141f5d74a | -2.58421 | -56.99371 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de61076d-4013-3575-b663-03b644b1e66c | -2.58375 | -57.57522 | 2024-11-02 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca8c7e47-97f7-3262-b919-cc5c8e5f4709 | -2.58243 | -56.99131 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54fda943-9783-3b8d-83cc-f98311c4ee2a | -2.58053 | -57.07006 | 2024-11-02 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd136d75-d177-3109-b974-e6058de67d7e | -2.50629 | -57.63484 | 2024-11-02 05:27:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a740f19a-bed8-3e77-bce5-cfa0e53fccf0 | -2.50563 | -57.63919 | 2024-11-02 05:27:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8710915b-b8ea-3c6f-8f80-ceab7faad4b5 | -3.6877 | -58.50651 | 2024-11-02 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9087603a-759d-3358-8256-d957331cd2ee | -3.68708 | -58.51058 | 2024-11-02 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df48b087-72e0-3553-8533-f147c26eef3f | -3.68412 | -58.50597 | 2024-11-02 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42cf7d7c-265f-3c60-8f68-011129234c75 | -1.9171 | -61.73024 | 2024-11-02 05:27:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e4b3500-21bb-39cd-8ae9-23ca20ba9a20 | -1.89923 | -61.30537 | 2024-11-02 05:27:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f3eff58-7367-32bc-951c-a36c67b32918 | -0.75849 | -62.90025 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4256c594-3919-30c2-91f1-d9b8e02ac6f6 | -0.75562 | -62.89594 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6c03f9-cdf4-37c3-b92c-4244fa0c67ed | -0.75503 | -62.89971 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf2984f2-cba9-3af3-9bd5-edcf566366d1 | -0.75444 | -62.90348 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce25abc8-c98e-3b28-9a08-01478594d33a | -0.75216 | -62.8954 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d1fc2f6-2712-3633-a389-ce52c46ca4ce | -0.6994 | -63.20817 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5967a21d-0295-348d-b83c-8d254cfae06c | -1.07335 | -62.65086 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59e4c085-c205-3a16-9f90-8f75cb559ce8 | -1.06876 | -62.65768 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9e51c68-c176-3713-b2c0-b06d5cffd44b | -1.00885 | -62.79604 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 940699dc-909a-368f-b55c-20c4a9cca34e | -1.00827 | -62.79976 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b151229-fb8e-3257-b302-c54be517b24b | -1.00483 | -62.79922 | 2024-11-02 05:27:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e78da82-a261-3483-a95e-5af4da1bd781 | -2.67611 | -54.02618 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88de95ac-8d84-350c-9ed9-3bd3d97e6ecd | -5.1492 | -47.71703 | 2024-11-02 05:27:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08c28996-d1d9-3d99-90a5-52e01572ada6 | -5.149 | -47.71567 | 2024-11-02 05:27:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38add0a7-a83a-305b-b17d-065f308a9670 | -3.46058 | -47.66709 | 2024-11-02 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f1d5b4-7363-32cb-af03-482347841b9d | -3.45604 | -47.66446 | 2024-11-02 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 33db4b83-a820-3803-a57f-7c1c82724dcf | -3.45354 | -47.66534 | 2024-11-02 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbe15029-5858-3c63-8c3f-880ac5519a26 | -2.91173 | -48.61559 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61ee2c9c-8e0a-31fb-8285-b4b9a62ff68e | -2.91089 | -48.62136 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ee69b6-c31d-3f14-815f-79ee7920edcf | -2.90961 | -48.61514 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45532952-0dc4-36ce-b9cf-58cb74246f34 | -2.90921 | -48.6328 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 132c06bc-f000-3662-b771-fce2f3dec0d6 | -2.90873 | -48.62092 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb7b3332-0ba0-3e05-a58f-bb5d9bfe30f4 | -2.83847 | -48.44601 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45f7abcd-3ff5-33c3-a9d8-cc7ab861e07c | -2.83169 | -48.44501 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edac3943-f422-3730-a330-ffc33fa80a1c | -2.78277 | -48.57125 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8ab238d-acbf-3eb4-afda-cad545a5c6bf | -2.78188 | -48.57717 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d8eb5ba-55a7-35bf-b8d2-4594d84489d0 | -2.78099 | -48.58301 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0889ff86-f5e5-3234-b63a-1ef0499b7135 | -2.77885 | -48.57114 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd12dbc7-467d-32e0-b45f-765b09bb2be3 | -2.77799 | -48.57706 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5760e9e5-ad0c-3fc9-83d0-0a3cb754384d | -2.77769 | -48.72021 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2137af6f-b01f-3088-86e4-755061b0c595 | -2.77715 | -48.5829 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5aaee015-d805-37f2-bbc1-3f8df7baf395 | -2.77686 | -48.72593 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5d3973d3-8fe3-31e5-bf67-74be6e7ea2b5 | -2.77606 | -48.57025 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2401196a-8ad6-36b6-8dd5-9f7d9a4b5278 | -2.77516 | -48.57618 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 916cb84f-1ea9-3cf6-b3d5-2930b5e7a2b3 | -2.77396 | -48.71897 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1025fc6e-f6ca-3d3a-8d41-30643aece913 | -2.77309 | -48.72468 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 95c225f3-a23a-3ce7-b275-f40ad0c7627f | -2.7702 | -48.72492 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97209975-0e41-378e-bfdd-549921528e60 | -2.73549 | -48.74841 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a158ab3-41c4-3a30-bd7e-e3714487710a | -2.72884 | -48.74741 | 2024-11-02 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ed59917-163f-3a03-9bf8-646902111fef | -2.62818 | -47.96569 | 2024-11-02 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8aaeccb-a95e-3c97-b08a-99884520d3b5 | -2.62119 | -48.33624 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b64cdc2-df7e-3291-b1f0-aa2dfcc4540c | -2.61699 | -48.32885 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 698d831d-1195-3089-a519-1609b3532ec4 | -2.6161 | -48.33494 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 266fcc76-506d-3ca4-8f41-d2d29a30fb0f | -2.61438 | -48.3353 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 620ead57-65e8-36bc-ae93-0d2ca6ce59ce | -2.5547 | -48.17577 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94e86785-d6b3-396b-847f-4f44da33bd28 | -2.55468 | -48.17501 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd45f96e-f3ff-3d00-bc5e-11aedbc09ac5 | -2.55379 | -48.18103 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52330cc0-548d-3e75-88ea-c2ee7e31307d | -2.54781 | -48.17499 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e9e123b-3744-3c32-b160-82785827fdd8 | -2.5478 | -48.17415 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cd3a9c5-5672-3050-9831-38f6c4408600 | -2.5469 | -48.18021 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eb14a91-9929-37b7-b449-c03faa1fb9c8 | -2.45918 | -48.4957 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1023d02d-ec69-3e75-a326-f73e2312d436 | -2.45832 | -48.50163 | 2024-11-02 05:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49bf1dcc-d272-34e5-9f9e-a8aca214f068 | -2.45526 | -48.84701 | 2024-11-02 05:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b5203bd-b224-3907-a74d-0a92dc21a7b5 | -2.44868 | -48.84606 | 2024-11-02 05:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1bc84d3-72f4-33cb-8dc4-c4445718cd08 | -2.36657 | -47.63075 | 2024-11-02 05:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee49fe69-3426-37b9-ae86-20db771e45bf | -2.36324 | -47.62794 | 2024-11-02 05:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 98187a27-a64d-3d90-9a0e-c73fddddc810 | -2.3622 | -47.63479 | 2024-11-02 05:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ee8d734c-3130-3330-954a-2e12effcc6ce | -2.35549 | -48.41988 | 2024-11-02 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1e5cd7-201c-3e66-a3e4-4c7b5f196bcf | -2.17647 | -48.72687 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3db0ad30-25ff-38dd-83fe-10003a88919b | -2.16818 | -48.73706 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8291f5d-de9a-3cb7-9841-37a8c2ebf8d8 | -2.16412 | -48.71912 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 889ce035-921f-3c96-9a68-377482284836 | -2.16328 | -48.72478 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bd04e80-9c4c-3d4d-8bea-a4c9ad45c74a | -2.16159 | -48.736 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d227bd0a-45e7-3f12-b2ed-2cfa127684a7 | -4.93535 | -49.15162 | 2024-11-02 05:27:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8e2d2fb-7790-3d0f-ae1a-cbbe76211a06 | -4.93451 | -49.15747 | 2024-11-02 05:27:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16336559-f7db-3a09-8d9e-40f19e18c8bb | -4.93107 | -49.15347 | 2024-11-02 05:27:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ead64b2-cad8-33e6-b138-7c26d7e875af | -4.92782 | -49.15659 | 2024-11-02 05:27:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README90.md)
