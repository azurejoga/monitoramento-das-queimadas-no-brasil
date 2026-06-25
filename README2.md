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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e2beb4d-f0f9-3993-88c0-cc37467c573d | -6.7541 | -46.303799 | 2026-06-25 00:23:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3b3191-b37d-3017-97a7-482f56b4cd52 | -9.1982 | -45.318802 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f79f52bb-f48a-3bf0-8447-45ae6583957c | -10.3569 | -50.114201 | 2026-06-25 00:23:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9c0663-912f-3b87-8f33-c8e64550ae6b | -11.2543 | -43.326599 | 2026-06-25 00:23:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 654bc2be-a879-3716-980a-2664ec49fc70 | -10.6042 | -47.157001 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b96cfc0-f8db-30a1-a244-8de0cbea8ced | -10.5963 | -47.120201 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d77d07f-a597-33fb-9b8f-f65132b97515 | -12.8406 | -44.3559 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f557c7d7-1fcf-303f-833f-c49b9b37e234 | -5.7908 | -45.041401 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c20103a3-e290-321e-94c4-698a061c2d71 | -12.7311 | -44.4659 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 364e6d2c-34ed-3e5a-a8a5-64a2ba31de5c | -8.6872 | -47.860901 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 091c685b-90dd-3ae9-beef-7be72fd7159d | -5.8152 | -45.057899 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a4c8585-5bcd-3634-a20a-9809aa18e8fa | -12.7377 | -44.448898 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee86001-9b78-36df-a807-5cc2e942acc9 | -7.7666 | -44.623299 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 135b99ad-a5ff-38fd-bd73-72658df2c1ba | -12.1351 | -48.268101 | 2026-06-25 00:23:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61c42e20-ff41-333e-a1bc-e6cbd13395e9 | -15.761 | -43.2346 | 2026-06-25 00:23:00 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1b5fbf19-730f-3783-a658-55cded642d29 | -17.344999 | -42.625099 | 2026-06-25 00:23:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 85573965-a0c5-31d3-9cfe-2c351663d274 | -10.5944 | -47.111 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f2d29bd-7e52-3423-af63-ae3d0f8b4762 | -17.343399 | -42.617802 | 2026-06-25 00:23:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d1a7f379-7b97-3e82-b750-37c486120772 | -8.6753 | -47.8535 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c81bc9a9-1ff0-37bf-878c-d33c6f4cd23b | -17.124701 | -41.346199 | 2026-06-25 00:23:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de1a10e0-c372-3798-911a-dd4d29797875 | -10.5945 | -47.1591 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27a126f1-bf16-3e5b-805d-a8f9bec475e4 | -9.1998 | -45.326199 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e24f8b15-5e3f-3f70-88dd-49d8c8008a99 | -6.3099 | -44.649899 | 2026-06-25 00:23:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e9c9d5a-0953-35d4-a304-7b7809410560 | -17.3466 | -42.632401 | 2026-06-25 00:23:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 098355c7-365a-317b-8442-23d7ec1978e2 | -5.8069 | -45.066898 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef7ad29-66c5-33d0-ac92-75138a5cc74f | -11.246 | -43.3358 | 2026-06-25 00:23:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 89aaecf1-61a9-3f95-ab63-4667f631a7f6 | -9.5392 | -40.3214 | 2026-06-25 00:23:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 36cc98ef-3a82-3a32-bf26-3a40d151ea0e | -6.9781 | -42.882 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de0449f1-46c9-31a4-90ff-46b9ca26e08b | -7.7438 | -44.613701 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb6928a2-6140-3e9e-a0fe-73e6e1a1d7d7 | -11.9161 | -44.1717 | 2026-06-25 00:23:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cca805c-a68d-3417-ac5d-ea47a80f2cc9 | -5.8194 | -43.583801 | 2026-06-25 00:23:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb5b3274-92eb-3644-9c75-4b0b930c3c25 | -7.7552 | -44.6185 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88bcfc05-fc2f-385a-92d7-10a30e185151 | -13.0584 | -53.3396 | 2026-06-25 00:23:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13a30c16-d3e3-340f-9174-94cda8aec368 | -11.9088 | -43.398201 | 2026-06-25 00:23:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed5ebea-2a6b-3d21-8355-651144e0ecf1 | -12.8422 | -44.3633 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9be95551-f311-357a-b980-baf92f92fb34 | -10.5866 | -47.122299 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72d614ca-f226-3d02-97bf-b0b0da7cc78a | -12.3154 | -46.733299 | 2026-06-25 00:23:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40d478fe-cf5c-3643-a92d-c0023d870d7c | -8.1303 | -47.891201 | 2026-06-25 00:23:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4376084f-4a16-3fa1-8971-0090ba51a66a | -8.6794 | -47.872601 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89086d66-ac15-32ab-87d4-14a1205bf371 | -10.614 | -47.1549 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e96350ff-e71d-33ec-b0a9-04b329f09c67 | -9.2096 | -45.324001 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5b54bd-479d-39bc-a31c-5b7bdd7f145f | -5.8226 | -43.597599 | 2026-06-25 00:23:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86e92ad9-243c-3522-9f2d-390bbb59dece | -11.8805 | -51.748402 | 2026-06-25 00:23:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59c676f2-1d4e-3af0-b663-ae814184e503 | -11.9103 | -43.405201 | 2026-06-25 00:23:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad215463-b2b0-3b97-9810-153ab6c06b1c | -12.7491 | -44.454201 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc2cc663-6e71-3761-a808-1e90652d8e96 | -5.7594 | -43.187901 | 2026-06-25 00:23:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f062ae53-a146-3834-aff9-88097356a038 | -10.618 | -47.173401 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 162a3963-4dd7-3b9e-8dc1-cab8cd2099bc | -5.8054 | -45.060001 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d061ef81-6767-3e44-9932-76102842e138 | -13.0632 | -53.365398 | 2026-06-25 00:23:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 214eb597-c74c-3f97-b20c-85b92c63a3d3 | -7.7634 | -44.609299 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a115ff96-0ba5-3720-add5-69bfc3e90dd3 | -5.8136 | -45.0509 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df19766b-078e-301f-960a-43216747a94a | -7.6286 | -50.215302 | 2026-06-25 00:23:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 417e1600-9c95-3b10-a591-230966e9542d | -10.5925 | -47.149899 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81e5ab71-d881-3048-9249-28edbf83f5c2 | -10.3697 | -47.3531 | 2026-06-25 00:23:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd160260-134a-3d74-aa8f-1007b3f1a853 | -6.97 | -42.891201 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ca279ca-a73a-33fd-aa50-cd3799078845 | -12.7425 | -44.471199 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a015397-297f-3c0d-a24d-90bfb32b9582 | -6.7574 | -46.319 | 2026-06-25 00:23:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7493966-42c0-36b1-a980-6da892b78479 | -9.1884 | -45.3209 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b64437f-20df-32a3-a160-0e336e34a8fb | -11.9145 | -44.164501 | 2026-06-25 00:23:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eebc0917-3c26-3d68-892c-40e2f2caa58b | -8.1205 | -47.893299 | 2026-06-25 00:23:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b195eab-fbc1-3ee1-b63b-dd265c68bc9a | -8.6774 | -47.862999 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2f9cad-6661-3678-8c0c-5a32cd5901b9 | -10.5886 | -47.131401 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30e54588-2a46-3844-9e94-2292c0b758a2 | -5.8038 | -45.053001 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f41b596a-8a18-3410-aace-2b4a0214541b | -8.6851 | -47.851398 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2af8837-a876-3484-86e1-ee4628ed0e8f | -11.9119 | -43.412201 | 2026-06-25 00:23:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 013364d0-c600-3727-a930-8d94d5a28102 | -12.1328 | -48.256802 | 2026-06-25 00:23:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c61e649f-887a-3b08-8a1c-bc11a29859f2 | -6.9879 | -42.879799 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e29aae92-a273-3540-9a8f-398f6fcbf422 | -6.7558 | -46.311401 | 2026-06-25 00:23:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a08a975-6e4f-32f2-ad6c-f6164bef01d8 | -7.7423 | -44.6068 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5645f954-336a-35b6-a0ae-404cde5a622a | -10.3677 | -47.3437 | 2026-06-25 00:23:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acd84e52-e23f-3892-94cb-9b57aaa609bb | -7.765 | -44.616299 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb6c7d3e-3377-38f4-bc54-2fc95fe8adfa | -9.4544 | -49.8349 | 2026-06-25 00:23:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad7589a6-74e8-3a08-9f6e-ae7335d67e5e | -9.549 | -40.319099 | 2026-06-25 00:23:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3da6edcb-91cb-347f-9d39-03399139c1db | -7.7568 | -44.6255 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83380b0f-7c6d-3395-98cd-000cc969729f | -11.2445 | -43.3288 | 2026-06-25 00:23:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c91e7c0d-315e-3e11-ad69-829767868047 | -9.5781 | -49.1134 | 2026-06-25 00:23:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89f74d24-a0dc-38f1-9e2b-3aa54e03ea0e | -12.7409 | -44.463699 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb04034a-c7aa-3b8a-af55-19082278186b | -10.616 | -47.164101 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42af5603-48bd-3e10-8289-3ab4b8a6a815 | -6.9912 | -42.893799 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38fcd5e3-1410-311a-864b-b959a458ad88 | -9.1868 | -45.313499 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e92ab814-9c76-3975-bb9a-3b0102875320 | -6.9814 | -42.896 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e1cb69a-2505-3457-ae9b-7d778308f2a3 | -12.7393 | -44.456299 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a90f19c-71db-3580-8195-b31527edba3d | -8.6892 | -47.870499 | 2026-06-25 00:23:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6b6ab1-29ae-33ce-9130-5cc52204912e | -7.7536 | -44.6115 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a23695f1-2989-3f59-8b31-b5a1fcea4859 | -7.7454 | -44.620701 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86c3521a-853e-3d80-8199-dd50fb3c6a83 | -9.551 | -40.327301 | 2026-06-25 00:23:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0396ce7c-23cd-312c-a222-0ea8cf94ad72 | -9.5471 | -40.310799 | 2026-06-25 00:23:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2cb13959-1cef-371d-8d05-d72671fed598 | -7.807 | -46.462898 | 2026-06-25 00:23:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77fc4340-a6d8-3d93-aa62-c29e540252c5 | -10.5846 | -47.113098 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 365d0c4f-eee8-33c4-a788-58581fa771c3 | -6.7656 | -46.309299 | 2026-06-25 00:23:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 646711e3-9951-3685-9bb8-2572ae2f80ee | -5.812 | -45.043999 | 2026-06-25 00:23:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51cdd31b-fce8-31b0-8d25-861e2cf7acf0 | -7.7366 | -44.171501 | 2026-06-25 00:23:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7e3fccb-ac7f-3606-99e6-36b734b73e9d | -6.5071 | -42.2271 | 2026-06-25 00:23:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b3ee4583-236e-318a-bc08-36872e663791 | -12.7507 | -44.461601 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 346746cd-5ca8-36e1-8f15-6a7ebf49037c | -7.747 | -44.627701 | 2026-06-25 00:23:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9cecb0f3-eea4-3f61-8c51-ad80a3a42065 | -6.9798 | -42.889 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8027cb7-8740-364d-833d-7703188f38e3 | -10.2935 | -44.693001 | 2026-06-25 00:23:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2878b28b-598d-3e65-945d-beb557960471 | -10.3657 | -47.3344 | 2026-06-25 00:23:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0c1d8f9-1e6f-30b6-aa2f-6cc8e07a0619 | -17.354799 | -42.622799 | 2026-06-25 00:23:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fbb94545-f1ba-3577-9860-b791492a273c | -10.6022 | -47.1478 | 2026-06-25 00:23:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
