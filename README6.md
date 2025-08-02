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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 976c2309-d6fe-3abb-855c-ff804dbf080d | -16.70923 | -47.57781 | 2025-08-02 03:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ae3d1f5-eefb-341e-a1fe-3b6e4556b92f | -12.67568 | -44.48676 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2dfd3949-54e8-35d5-ae6b-5dce9c7a2694 | -12.67273 | -44.48088 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc105810-d94c-3d4c-9439-bcb52e9006e8 | -12.67391 | -44.49575 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 729e9015-e43e-34a9-8c92-093f4b00a072 | -12.65124 | -44.49489 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| db47192f-4723-35b0-8fd4-93ff1647838e | -12.66588 | -44.53625 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd61c81e-5e0a-311a-a08c-766fd7b3f6fa | -12.44531 | -47.05874 | 2025-08-02 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2519cded-6b28-3800-bb5e-303ca23fea69 | -12.65396 | -44.53373 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6437c0fc-47c0-35c9-a166-637b70cf3325 | -15.8051 | -47.70864 | 2025-08-02 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da2bd428-741c-3abb-b717-b5bda3397691 | -13.21564 | -42.25521 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ad490ad6-5773-35f4-a388-05c0d1ec9c67 | -13.21631 | -42.25163 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e258a0bd-84ab-311f-a810-cbd64a1b080c | -12.66166 | -44.53472 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e4c23b5-8dee-32f6-9467-8679ca03ee91 | -12.67781 | -44.53875 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d08f6b5-e059-37ac-8ed7-3c846a5971a8 | -12.03107 | -44.02365 | 2025-08-02 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2dd9cf07-98f7-3a6c-a23b-8529311b897f | -14.79523 | -42.72566 | 2025-08-02 03:34:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cec2626-84eb-3076-b1b4-f32df3e839d0 | -12.67682 | -44.49113 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6cbe6ec-7d61-3f2f-a358-686d54be4b74 | -12.67266 | -44.54169 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99a4c2b2-d8ea-3c50-bfe0-13bad6fa3202 | -16.2483 | -48.95525 | 2025-08-02 03:34:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cda723f4-919f-3155-a7f1-738a153eb5f8 | -12.66708 | -44.49891 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7fceb84b-593a-348b-8ab2-f56ea20b44db | -12.66947 | -44.51817 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f5eae33-7e90-3365-a0be-4ed14333ed51 | -12.6704 | -44.52243 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1804c6d-efe5-3864-b384-5a712f65bc48 | -12.65992 | -44.535 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5a16840-5986-3233-8d0a-d3a238923e13 | -13.06067 | -47.44505 | 2025-08-02 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8b0771c-e976-343d-b558-8b46fb07b60b | -17.91928 | -42.74191 | 2025-08-02 03:34:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c461c06e-2c14-3763-a34e-84b14138d650 | -12.67807 | -44.50602 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b21e1e0-9a5e-3e93-b9fe-d696b2f90027 | -12.67274 | -44.53298 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca34d879-8091-318c-a918-9c0337747316 | -12.67223 | -44.51348 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd8eeb9a-ccd5-3669-99b7-12aef3c02a80 | -12.65847 | -44.51107 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 93752d9a-9a93-3655-8768-02f89f268ea5 | -19.57254 | -40.78964 | 2025-08-02 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 110717a9-0998-3d4e-a52c-ef6b3b6fc7dd | -12.66947 | -44.52693 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f162bfbd-dcba-3b7f-a9c7-a1b497d3aa86 | -13.89699 | -42.13615 | 2025-08-02 03:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 004ca308-e810-3850-8928-3f465c643512 | -12.54133 | -44.71984 | 2025-08-02 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65ddc19b-e8f9-31ae-a9c4-7c646f8bb863 | -13.21764 | -42.25591 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9e9a6cba-42e6-353d-affc-b4e6b97ba300 | -18.23993 | -45.17031 | 2025-08-02 03:34:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c5c5284-0ad4-381e-b7f6-0c367a487ffd | -12.6787 | -44.53424 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5341cdc4-5055-3224-9672-4c18c21eb2e2 | -13.85047 | -40.86892 | 2025-08-02 03:34:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4f510757-deb7-3763-adbf-b102981d10ea | -12.66857 | -44.52268 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b7d7675-32b1-31a3-a9cd-89d4cea6a399 | -13.89615 | -42.13554 | 2025-08-02 03:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b694f0c9-a37e-3f97-bea2-89905c9635df | -18.2184 | -44.7061 | 2025-08-02 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e13e5de8-2e59-3d2b-b76b-5b789cd16632 | -12.64939 | -44.50382 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 755f044d-7360-38dc-86c6-61fa1342f5c3 | -13.89753 | -42.13328 | 2025-08-02 03:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66c121a1-1a4a-357d-9c20-c11f674b3237 | -16.24696 | -48.95777 | 2025-08-02 03:34:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ee554b8-8f99-3c1b-8d6f-c340a2cfb7fc | -12.67213 | -44.50473 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f8b77254-bb81-3495-959a-8a2c6c56327b | -17.22849 | -42.55014 | 2025-08-02 03:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c28f0ba-6b22-3925-950f-d6f85a471492 | -12.67774 | -44.48666 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 823c4a6d-f0cd-3bb3-a4b5-7c01880c4aef | -12.67543 | -44.52818 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c557202b-1590-3e7b-8153-e0c997d56481 | -13.21836 | -42.25226 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6f73a234-da35-3ec3-ad26-bf8af138b20c | -12.66905 | -44.49878 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 00403621-f387-320d-ab79-993ceedd231a | -18.53129 | -49.50508 | 2025-08-02 03:34:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 47117124-387a-3f10-b606-e9b9c4f1cf5b | -12.67315 | -44.50901 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8a20ea8-ab80-3a04-9247-dd7720f407f2 | -13.17166 | -42.23536 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66ea11a8-fde5-3de1-b961-d8aa0240cfda | -12.65432 | -44.50075 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 75f92298-516a-33d3-8b42-1dcbd1d7ea8f | -16.68633 | -41.01757 | 2025-08-02 03:34:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22e68563-e8bb-37c8-ad58-bf3d0edd74ae | -12.66496 | -44.48852 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 96114058-15d4-37a4-8f60-9026709c8e5f | -12.65757 | -44.51559 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c314f76-92e6-389b-a4c1-73f51e56e117 | -12.66127 | -44.50642 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0a483382-65a9-3426-a1c0-ed34235493f4 | -12.66813 | -44.50327 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 033b4032-a692-37c5-a994-ad7ec56278d6 | -12.67451 | -44.53268 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 328e41ae-ac9f-39ab-903c-fb571a93ea04 | -18.52858 | -49.5042 | 2025-08-02 03:34:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3c16bdb4-7da8-3dec-8afb-abe0d0869111 | -12.67453 | -44.52394 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf5bb3cd-ebd6-31f2-a4f5-476b4b05ebdc | -13.0592 | -47.45179 | 2025-08-02 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c25b0bfa-a30e-340b-a8d9-317503a95c60 | -13.21315 | -42.25171 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b79af952-74ba-39f7-a628-6a7cd658fbd0 | -13.89835 | -42.12897 | 2025-08-02 03:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e8e5666-c332-3145-a3f8-d0966d58dfca | -12.66025 | -44.50208 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6644cb1b-9c52-3e1c-b384-92f9497a9f19 | -12.67095 | -44.54202 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d38a3cd5-f4d0-3eb9-9281-c4d091204248 | -12.44403 | -47.05851 | 2025-08-02 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e833227-9a0c-331c-9879-68eb5c2798b5 | -12.65347 | -44.51412 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 63451fb2-013e-37cf-9166-8b7840de54e3 | -13.21914 | -42.24826 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8db8df5a-8edc-3816-a124-d341b5a78029 | -12.6544 | -44.50961 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4386b4cc-fc3c-369b-bd9b-975abfc119d5 | -12.44815 | -47.04525 | 2025-08-02 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16d34696-78b2-3595-80dc-6c1f8b9d193d | -15.0599 | -43.87403 | 2025-08-02 03:34:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2886f907-c7aa-3dec-9949-4f0133507b79 | -12.66997 | -44.49429 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6cfa6928-ea4a-3b5d-bd96-ff557eaef719 | -12.6748 | -44.49125 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ab7dbf9b-c0e1-39ce-9742-3f1986c4e030 | -11.94844 | -46.6753 | 2025-08-02 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3bd2780-7da1-3feb-9d47-40b6d4a845c2 | -12.66404 | -44.49299 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1947f585-40d3-3fea-ba10-756f6e3c4942 | -15.36833 | -44.2837 | 2025-08-02 03:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 907fe623-aa46-385c-9c35-19bf1df62d89 | -12.66311 | -44.49747 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 702db4fd-0d2b-30d8-b86a-6b7dd518b841 | -12.65162 | -44.51429 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 26717c6a-a1d6-36b9-a7e2-66aafd5b9257 | -12.67363 | -44.52846 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7285be19-909e-3f93-a306-dc07d5f1b6c3 | -12.67407 | -44.50455 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 89c0feae-2913-32d8-883c-9446e8dc6257 | -12.6561 | -44.49181 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 676c82e2-6dff-3de4-8773-abf329084f6b | -15.37388 | -44.28511 | 2025-08-02 03:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24aab192-5a0d-3b29-a6d2-d88805cbf770 | -12.65032 | -44.49934 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7a203c24-5ae3-3719-bc6b-e6f9790e4f4a | -11.96461 | -46.66631 | 2025-08-02 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b447c827-9361-3470-b249-e7346bff3df1 | -12.66619 | -44.50341 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d5fd780-0c29-3f77-8211-5e3dcadb6664 | -15.06064 | -43.87033 | 2025-08-02 03:34:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15b9faab-644e-3061-a790-e37155925227 | -12.6759 | -44.49561 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83c82fbc-8595-3cbd-869b-236a79cf3bce | -12.66797 | -44.49442 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| df63817f-1862-32d6-a5d0-f3bddabfd8d9 | -12.66115 | -44.49759 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 62f11fbd-7ad2-31bc-add1-7be4944b30c7 | -18.53298 | -49.49827 | 2025-08-02 03:34:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| af8312b9-9b56-3a88-9127-bae15a604f66 | -16.68716 | -41.01313 | 2025-08-02 03:34:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30631154-5872-3069-b74e-df00a7de3331 | -12.67657 | -44.4823 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 17cabdc3-16ae-3d03-bec9-bf28f453647d | -12.67035 | -44.51368 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0e5b48bb-97bd-386f-b07c-eaef0ac5ce8a | -12.65216 | -44.49044 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53b0bcb4-0fd8-356f-98a4-6fc7e28a0365 | -15.36911 | -44.27987 | 2025-08-02 03:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6105de8-8eee-317b-856a-848d019cf1c5 | -12.65569 | -44.53348 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0ada89e-ab13-3218-89c5-779c3eac981d | -12.67185 | -44.5375 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a04dd561-9f4c-3e9f-821c-cfec828a827c | -12.44549 | -47.05178 | 2025-08-02 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79a6cf81-44e1-3d78-b6d4-ecbaad1fd6cd | -12.03279 | -44.01508 | 2025-08-02 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b48d31e-6bbc-353c-bd95-daacc02e6c60 | -12.66537 | -44.51668 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README7.md)
