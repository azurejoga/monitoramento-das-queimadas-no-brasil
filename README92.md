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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61221cf6-ad40-3f2d-adaa-9ad9f2607ac1 | -21.5984 | -47.38998 | 2024-10-09 04:17:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8017d4d-66a4-3284-ba45-66c27686a0eb | -21.59755 | -47.69035 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22dbeac6-d156-3a38-af93-03361f22829c | -21.59721 | -47.71346 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4584feb0-0609-323c-8a38-63766cf0c1aa | -21.59694 | -47.6941 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b82ca94e-94ab-3764-ad5c-aba8c0252a2d | -21.5966 | -47.7172 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec673a37-bca2-33be-8530-a4be28a6021e | -21.59599 | -47.72094 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc75375-f60a-354e-83d6-f9fa696a26fa | -21.59538 | -47.72473 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94ef5937-e721-304c-9e58-82e743fd6112 | -21.5945 | -47.70906 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97feb41e-f06b-3c4f-922f-9a41c3bf49d9 | -21.59389 | -47.7128 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 581d1cf7-1d91-3eb5-9306-526bb51f53f4 | -21.59117 | -47.70842 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b40b217-e871-39ad-93f9-858fabe902ac | -21.59116 | -47.3925 | 2024-10-09 04:17:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed345f0b-5e36-31a5-b897-e42b210e4685 | -21.59056 | -47.71214 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 242fbd26-e4d0-3351-824b-b5202d8d7e68 | -21.5823 | -47.74177 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8278799d-9e1e-3c43-8fea-efd1060ac205 | -21.58211 | -46.98235 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 34629b24-7981-3223-8ca6-7c7b01678398 | -21.5807 | -47.87778 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 28dc0a83-1a8f-318d-be05-af64c7f5e11d | -21.57821 | -46.98545 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0185f737-8a97-375a-9b51-f9b157ca800d | -21.5776 | -47.89672 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2af5b48c-56ed-3f42-a34b-fec6adc7c870 | -21.5724 | -47.90745 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e8784f9-3529-3f4f-84c1-d61f05bd38b8 | -21.56499 | -46.98306 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8333fe70-b713-3abb-9b84-d7839bd4b6bf | -21.56286 | -46.97507 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 479ed0f2-dc9e-3b68-a9ff-6da9704c7483 | -21.55898 | -46.97816 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34002965-724c-3b1c-951c-fb2b93517c79 | -21.55567 | -46.97755 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73e68cc0-ba5d-37d5-a4a9-28754162ba12 | -21.40776 | -47.80636 | 2024-10-09 04:17:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b998c9ec-7b94-348f-a2ab-f9445de5ab5a | -21.40443 | -47.80573 | 2024-10-09 04:17:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f81fac-f90b-30e0-95e6-24b98dcd44aa | -21.36334 | -48.03268 | 2024-10-09 04:17:00 | NOAA-21 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b3f1a70-c1a3-33f7-9c13-64d3c396452c | -21.31758 | -47.6079 | 2024-10-09 04:17:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5838eaeb-7848-3d62-8959-b689b4d0e237 | -21.58996 | -47.96091 | 2024-10-09 04:17:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4aa82fa-5a30-376f-b081-e12af0455d42 | -21.58304 | -47.90555 | 2024-10-09 04:17:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5790c888-5a1a-376a-9cae-49b505207e69 | -21.58156 | -47.89355 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1691da74-b35c-3d1b-b0b7-62665c7c1fc6 | -21.57946 | -47.88536 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| adb98873-2b6e-3e0c-a02b-5145e6058fb9 | -21.57697 | -47.90051 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c705601d-d401-38c7-bfc3-361e6ff51ac0 | -21.57674 | -47.88094 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63797d37-96a8-310d-b9b6-3076de48a2ec | -21.57635 | -47.9043 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f97aecee-865c-346a-8934-d17a5185efa1 | -21.57512 | -47.91187 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b07944a6-0857-3a03-9241-6d46205cb739 | -21.56866 | -47.93022 | 2024-10-09 04:17:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cafe9ab-54ab-3c11-b262-343dc4aed01a | -21.5794 | -46.97804 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6be3fce4-04ed-3d54-9887-6882b1bc3949 | -21.57881 | -46.98175 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db095d80-4d9b-3087-a7be-5487e3da5f66 | -21.5755 | -46.98114 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a63e8799-84ef-3a73-ad61-ce92ed4d0125 | -21.56948 | -46.97625 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7598eeb4-4811-3d6c-9882-6b5486de5b76 | -21.56889 | -46.97995 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cda1a12f-eae1-3e56-9cde-e335fab26b86 | -21.56676 | -46.97197 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d1d38d6-289b-3827-b636-c373ff2d384f | -21.56617 | -46.97566 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 279cfb55-65f9-3789-901f-fbe7f89cda99 | -21.56558 | -46.97935 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79f7415f-ce93-39d9-aa42-3b5d325f04af | -21.56441 | -46.98675 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d356e1ad-51a7-3776-9a5f-64b9cea4ff23 | -21.56228 | -46.97876 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abe301e8-353a-3bad-8f32-e6ddf7db0fd7 | -21.5611 | -46.98615 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 058fa45d-ff66-3935-ac02-0b9ed3b90e17 | -21.55508 | -46.98125 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e743f1ca-87c7-3c6c-a70a-c4eed9ec1ea7 | -21.30007 | -47.21361 | 2024-10-09 04:17:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 51b2a90a-48fc-3248-8d65-0098db973e29 | -21.29735 | -47.20932 | 2024-10-09 04:17:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48569a04-617b-3543-9f41-3b9510906f17 | -21.29676 | -47.213 | 2024-10-09 04:17:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0c1f061b-f059-3dcc-80bb-1a063170da88 | -21.29404 | -47.20872 | 2024-10-09 04:17:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1e958cde-b53a-37f8-81d8-eb03d80f459b | -21.29346 | -47.21239 | 2024-10-09 04:17:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4559889d-9056-3a56-828c-6d096ce61667 | -21.67565 | -47.71207 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a0202c8-47e0-34dd-9d9e-77428a5d5d04 | -21.67503 | -47.71583 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 055dd79f-7758-342d-9053-03786cc00fbc | -21.67232 | -47.71143 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fe39f75-bbb2-3134-896b-0c93e96dd3bc | -21.67171 | -47.71519 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 8109ae0c-873a-3064-b821-eeaba8caa133 | -21.66961 | -47.70702 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 677913f4-e1e0-3641-9209-99c93ce76df2 | -21.66899 | -47.71079 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f76419f0-5d5b-3b4f-955b-01b6469727bf | -21.66838 | -47.71455 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 9a831816-2861-3955-b562-ca284df12b2d | -21.66629 | -47.70639 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33d12f00-27fe-377f-a197-542c3ff57840 | -21.66567 | -47.71016 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73ab3b4c-c21c-3083-a8a8-76300e5c2a40 | -21.66505 | -47.71392 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 574.8 |
| 3d0d5945-d683-31c7-b686-d353588e3a7d | -21.66296 | -47.70576 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bfe0645-2bfd-366b-b792-9a4e7a76b22a | -21.66234 | -47.70953 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e48c475a-28a7-3c82-84a3-a483df2dc9c7 | -21.66173 | -47.71328 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 574.8 |
| 87c98169-e41d-33be-a87f-3f65afa90a13 | -21.65963 | -47.70513 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 453abcef-6f39-3324-8a89-edcd013a2a67 | -21.65902 | -47.70889 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 76275961-a718-3520-811a-bf15c74e7929 | -21.6584 | -47.71265 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 04e1c98a-55e9-3f31-a0b5-a56bb267bbeb | -21.6563 | -47.70451 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 61ae5ca6-c215-3e8c-b7ba-4d91fd8ff153 | -21.65569 | -47.70827 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c383e28b-b57c-30bc-bd61-0cd952175d6e | -21.65507 | -47.71202 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 144.7 |
| a57fa569-1478-3e8b-a7b0-c9a994dd0b5a | -21.65446 | -47.71578 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 7e306432-19f7-3ca5-9318-581841e83994 | -21.65298 | -47.70388 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44b58a12-2047-3c34-9b33-dedd1fd8191e | -21.65236 | -47.70764 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d45d547f-6554-33b1-a896-ac14a325fbd0 | -21.65174 | -47.7114 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 544f8ea9-26d2-3ed7-8428-9adee307c578 | -21.65113 | -47.71515 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ccb6373-00a3-32a9-856a-9c4bd80b5713 | -21.64965 | -47.70326 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0395f727-a40c-3f60-93f7-112ee611a2eb | -21.64903 | -47.70702 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4c8d1de-1abf-33dd-8421-cd80244987cd | -21.64842 | -47.71078 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa8a568c-9b3e-3e3e-9e78-aa9f2b0e34b2 | -21.6478 | -47.71453 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc4b54f3-7b7a-3648-9727-035f53dac178 | -21.64694 | -47.69887 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 015a3ee7-e89c-3810-9136-3061114fdd14 | -21.6457 | -47.70639 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b31591a6-d5e1-37b7-96e7-cd0d0dcb4bad | -21.64509 | -47.71016 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e4d043d-5aa5-36ef-8d0b-d1f1b62625aa | -21.64447 | -47.71391 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee357c65-000f-35d2-b330-336712e4708b | -21.64176 | -47.70953 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe38eb3-e7c0-3a35-b471-dca378ad82da | -21.64114 | -47.71329 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9acb67fd-a892-303b-adcb-f037f79a1d65 | -21.63843 | -47.70891 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c753e9b3-65cd-3b3e-bd6b-599c5d98afed | -21.63781 | -47.71268 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa74a13-0a4b-3853-ae86-6a7bafa85349 | -21.63572 | -47.70452 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32b3d6ad-d995-38fa-b8b6-642217a60f65 | -21.6351 | -47.70829 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df780a64-7ddf-3948-aee9-e5a734ec2bbb | -21.63386 | -47.71582 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0339df14-6302-3dc4-a677-54d69c563320 | -21.63301 | -47.70014 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c336d3cb-ecd8-3525-8555-732c2587e543 | -21.63239 | -47.70389 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 097a25f6-f1ff-39c5-ba67-924c50055b3d | -21.63177 | -47.70766 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63ef0c0f-cfa9-3b28-87c6-fe6642b2c8f6 | -21.62968 | -47.69952 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0955925d-bcbc-310e-862a-50d8987ff41a | -21.62906 | -47.70327 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 453d0dc7-2be6-3148-b0ab-4c95c5a6de12 | -21.62844 | -47.70704 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2307845-cd80-37f7-bea5-6ddd5920ef3d | -21.6269 | -47.69965 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1afc9896-78d9-338e-b644-862f4ea09edb | -21.62629 | -47.7034 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b47370d8-6a26-3346-960c-78e0c1b23372 | -21.62568 | -47.70717 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README93.md)
