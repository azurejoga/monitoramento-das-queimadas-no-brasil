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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e480376-329b-36c9-8843-7027d6b4fd55 | -7.13859 | -60.13153 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aae23fb1-05e0-3b1b-a79f-97518e5595fc | -7.06931 | -59.20466 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f5ae81b-1e8d-3b60-b6e7-30d457edf4ec | -7.14265 | -60.12822 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37212923-a469-357c-b2a5-01c5db34c100 | -6.244 | -55.36383 | 2025-08-13 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adecac6a-e94f-3188-9a31-016a013fbcc0 | -6.09286 | -59.93475 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 976fafcb-72b9-3cba-bf7d-dfb4fafd4b63 | -7.13343 | -60.11897 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3364212-5bfc-3b3e-b827-ae59228da64a | -6.07603 | -59.93647 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f367c52e-6fe6-3d9b-856e-b45e56ac2ce3 | -6.10323 | -59.93642 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71cfcff4-7431-353e-a9d4-345de826489c | -6.92761 | -59.14772 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e32a0a67-a92e-39b4-9965-4de5b6807555 | -6.09689 | -59.93149 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c0e7a24-2f07-3647-a018-ea32a412e67d | -6.8957 | -59.13854 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1f728396-3349-38cb-a0c7-85ccf23ea2ae | -6.91205 | -59.12822 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| efd80067-bc13-37dc-abc2-8f8b8b04b85a | -7.07196 | -59.20254 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9672c0d9-d23e-32bb-b628-b8e2f3a5bde0 | -6.10726 | -59.93315 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08de1ff1-da70-357f-9200-6c0c5ae00ea3 | -6.09574 | -59.9391 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30885cfe-5189-3cb2-97bf-6097f61d6906 | -6.87336 | -59.13953 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 23551999-59ac-317c-a0f1-0c8e3902191e | -2.90305 | -48.25274 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c774ddbd-41f3-3907-aac3-6b97e0d65e86 | -7.06869 | -59.20882 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9781892-a720-314f-985e-dc08749d4dc2 | -6.11188 | -59.92609 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10e41153-a86d-39c8-8a08-398e85a8a418 | -7.62123 | -56.71665 | 2025-08-13 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e57899a-e472-3431-b939-e77c92a0b1b8 | -5.8844 | -57.74383 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e13877d3-d652-30dc-910d-071d2ac08e4b | -2.90249 | -48.25775 | 2025-08-13 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| aa177500-786f-3061-8d06-171538a48841 | -7.14544 | -60.12438 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 45e1af4a-5343-3491-b21c-509dc9cebfc9 | -6.9108 | -59.13657 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8fa0a0d8-9008-3bd4-90d3-6dd1834d2445 | -6.10784 | -59.92934 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2e2a93-ea4d-311f-93ee-c8cf59578e65 | -7.0879 | -60.02168 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce69c447-7df8-35c4-8021-7a148b917226 | -7.13513 | -60.13099 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58ebae3-8fb0-3e08-981e-28d3512541e9 | -7.07654 | -59.20571 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cebfb69-554a-3910-bce6-4a9ef0f3ff2c | -6.8806 | -59.14059 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 45db52df-9990-383f-a213-47b91f327b55 | -7.09368 | -60.0305 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73d71448-b6db-3945-b4f0-3fab99fed5f8 | -6.90718 | -59.13602 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 6b9404fc-654e-33dd-852a-c56149e7f2e1 | -6.88784 | -59.14166 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6c5c0198-b7cb-32f3-ae25-6d08347884cc | -6.91504 | -59.13295 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1253a773-4eb2-3a5a-8bbf-fc83361815a0 | -6.88846 | -59.13747 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| cd11c1d7-83b8-3b8e-9394-a659f0f58265 | -6.09165 | -59.92712 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 963622cf-6eba-38d6-8f5a-a7302f1a0705 | -3.43656 | -49.04717 | 2025-08-13 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0990cdce-474f-3d2e-a1d5-3f8f5d109f13 | -5.85653 | -52.11074 | 2025-08-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1994cf9a-2dbe-337a-afed-6e56d5938787 | -7.13918 | -60.12769 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fa96f38-6001-3888-9bb8-7f9f8424aa42 | -6.09747 | -59.92768 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff220b1-3aba-3ab0-aa81-510bee09e6fd | -6.92824 | -59.14355 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d2bebd38-c9a1-3bc1-a7bb-8a7e02bff2e0 | -7.09774 | -60.02719 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfe574e8-5613-3672-81f8-e25de4fa4df6 | -7.08849 | -60.01781 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7aaa76c2-8303-3f29-a210-a5b030a59e2e | -7.07416 | -59.19686 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7e8182-c330-3628-9762-bd3e3a19d0d6 | -7.0677 | -59.20618 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e428a33-2664-38c4-98f8-df63add8f311 | -5.66409 | -51.3639 | 2025-08-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12707d69-3004-3dbd-9730-1918a705fa8b | -6.89994 | -59.13492 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c21b7618-b59a-3388-b39d-f508e1df9225 | -6.09919 | -59.93966 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af26d079-69db-3b5b-9218-88c1968c5164 | -5.85086 | -52.10999 | 2025-08-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b2b865f-1245-396a-beae-77613de950d3 | -6.90294 | -59.13964 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| d32fec25-08f6-3b2a-b5de-ecf6a10283f3 | -7.11847 | -59.84338 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99055744-bee6-3862-83be-04cb402b2fb5 | -5.88826 | -57.74447 | 2025-08-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f425d231-9887-341c-b2d5-ec224b5dfaeb | -6.88185 | -59.13219 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 93fba7cc-c9a5-3e89-b5d2-46aaa39ff05b | -6.10496 | -59.92498 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df1f9c2-ccb2-3883-a6da-135ce06e756a | -6.89806 | -59.14751 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 218b4567-10cf-30a0-b185-fc579ee43cf7 | -6.87212 | -59.14793 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 15be9fd6-d808-322e-8af0-7e81b4c9e9f0 | -7.12879 | -60.12608 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 872761d5-1f75-3608-ad4d-6ea7eb1a7a38 | -6.89395 | -59.12549 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25bd424c-09ba-310b-ae5d-1ac9a377b2ac | -7.14731 | -60.12106 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38960a2c-a471-323a-a18c-ff0f2d4bef10 | -6.10381 | -59.9326 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48811ed9-a1f9-3f47-b3a4-79c560f98267 | -6.8715 | -59.15211 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| bce2a7a9-464a-34ed-93f4-15e3788d1b49 | -6.10438 | -59.92879 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d9643f0-c271-3373-bd22-132f0a10b523 | -6.89869 | -59.1433 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8c7cb9e7-f44d-3257-ad0d-7e29c512b74d | -6.92877 | -59.30951 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 232d1687-e920-3366-a595-a36297b72d7e | -7.08501 | -60.01725 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862878a9-8d2f-3ecb-9f9d-738ef9e526df | -7.14602 | -60.12053 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d86fb45d-bb89-31ca-9206-80bba7895566 | -7.14205 | -60.13206 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62fb7cdf-4fae-3eb5-8820-9f1090708038 | -6.07544 | -59.94027 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac32dfc-b189-3f1f-9383-19473acbd533 | -6.10092 | -59.92823 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e4bfc8-d202-31a7-951a-e24328116bc6 | -5.66351 | -51.36806 | 2025-08-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e81cec3f-905d-3145-8b36-bfcb321a02e7 | -6.87274 | -59.14373 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 652f0227-4c6d-3631-951d-e8fee0111067 | -7.07292 | -59.20518 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e95c516-cce4-3a0e-b5f5-3bf5d34a6762 | -6.90481 | -59.12713 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 51108113-8b20-3e48-9dd1-9c945bf17da6 | -6.924 | -59.14718 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 199f4670-ff90-3e1c-a2a0-b68618a545f5 | -6.87037 | -59.1348 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5788198f-99c8-389c-a8b0-85ed298a8ca2 | -6.91441 | -59.13712 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 25a9d1a2-3a03-3478-9864-489698f65736 | -5.84288 | -59.92567 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5828492-2bca-3e13-80fe-a7af528a0bdf | -7.06707 | -59.21033 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26d23230-eb46-3c81-a77d-6f3665bd7585 | -6.09228 | -59.93856 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2f86a9-bf36-3190-bb33-14e828571da9 | -6.69701 | -59.14118 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3125da84-16ef-3470-b555-c1659fdfc945 | -7.12938 | -60.12226 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9841954c-686a-328c-b58f-0fda252996c5 | -6.87698 | -59.14006 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bc809e9b-f0d2-3b7b-a5cd-32f746fb008c | -6.90356 | -59.13546 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| cd17575a-a9d7-3bd1-a47d-fbd2b88d8c78 | -6.1136 | -59.9845 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36399c66-dfe5-3ecd-a9aa-decc69bb060f | -7.09544 | -60.01891 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5ec52fd-3c1c-386c-b2e9-5c5a0f4fa421 | -6.92463 | -59.143 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 988a6999-d61e-3d86-be37-67f2485aac8e | -6.87873 | -59.15319 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 0bbf7250-8650-3d00-835b-5a3a9f51972e | -6.09516 | -59.94291 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d37bc2da-03f8-3d73-95ab-636791d3edfa | -7.14671 | -60.1249 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6d151b6-785a-3a61-accb-fbdfd3e72922 | -7.08443 | -60.02112 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ddbdf3c-8e8a-3fee-b4cd-be6ad7371477 | -5.8533 | -59.904 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e5cf5ef-bbd6-311b-b11a-c437cef0c444 | -7.034 | -59.82768 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9654f73d-06bc-3e90-8c25-2432cbe3e402 | -6.86788 | -59.15156 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3488d02-63f3-3385-be05-49ec412b69cd | -6.89932 | -59.13909 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bc90467c-c71d-323a-8e20-e6c287907649 | -7.14037 | -60.12004 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebbc3c02-bcef-35ca-bfe4-3334f3006506 | -5.84978 | -59.92673 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2606e5c8-d194-399d-82fe-fde01b488c22 | -7.25111 | -59.99081 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ef56e9-dd6b-320c-a15d-4d35430a0305 | -9.06421 | -60.65157 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d3da046-b80c-3ec4-8bac-f2f74c7066fb | -10.34771 | -50.81643 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d74e9c7d-a53e-313b-a055-f6c3536d9659 | -8.94329 | -64.16003 | 2025-08-13 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 13045677-93aa-3031-883a-acfafa2d7f08 | -9.38848 | -61.53093 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
