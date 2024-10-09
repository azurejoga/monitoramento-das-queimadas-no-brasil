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
| 2bf935bf-8609-3772-9cb0-613912c5056a | -21.83343 | -49.16355 | 2024-10-09 01:09:00 | TERRA_M-M | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| bc34bb65-ad63-33b8-a815-f07746ddee2d | -21.8259 | -49.17455 | 2024-10-09 01:09:00 | TERRA_M-M | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| ee407a5a-34aa-3623-9b3b-1c9aa0f5a9fb | -21.82456 | -49.16503 | 2024-10-09 01:09:00 | TERRA_M-M | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 218.5 |
| 055ebf6a-58e0-3d5e-8887-e2debe98f679 | -21.82321 | -49.15548 | 2024-10-09 01:09:00 | TERRA_M-M | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| cb1b7264-e777-36a7-a012-4167a79628e1 | -21.80127 | -48.3628 | 2024-10-09 01:09:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 034c6a42-3d44-3cb9-aa68-bd61cc141cc0 | -21.78329 | -48.366 | 2024-10-09 01:09:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ac20c62a-f1c6-3333-af5f-af342c315b95 | -21.65737 | -47.70891 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee711ba5-ec49-3d3a-92ca-7a28289b48fc | -21.64974 | -47.7209 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 97f6a16f-1a7e-372b-92b8-89e375da08d6 | -21.64817 | -47.71058 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3d2b36b9-4e59-365b-8513-2cb31b12f35c | -21.64661 | -47.70032 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 86d5a9de-299a-3036-9808-5e32e717983b | -21.64504 | -47.69 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 4f45ce84-ecfc-35cd-8b08-7d0795af4de1 | -21.64346 | -47.67959 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 935cce41-6b7a-3d8a-ae82-eb97d14f59fe | -21.63898 | -47.71222 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a131e061-f77f-3709-b330-195660f929dd | -21.63742 | -47.70198 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a6651d2c-bdce-3e1e-a34f-605b2e4899d3 | -21.63584 | -47.69165 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9fc67969-c223-312a-b7e6-614da4972812 | -21.63425 | -47.68124 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 85db60fb-73a7-3ded-87cf-c844dec04c62 | -21.62978 | -47.71381 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b7a607bf-5e86-3218-bf55-94fe4287165c | -21.62822 | -47.70363 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b632d3cb-abc7-37ec-ba92-648b55015774 | -21.62664 | -47.69328 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 42ce6ebd-ebe8-370a-9c5a-9981878a01e2 | -21.62358 | -47.72058 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 479849bc-0102-3ce5-8073-7da41d28cb10 | -21.62205 | -47.71041 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| fab3acf3-22a5-3c54-8096-d40c8554c0ed | -21.62052 | -47.70015 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 4f690198-3b16-3840-859d-fc377719b260 | -21.61897 | -47.68977 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f81c29b5-d28a-36bd-8121-3a936fd5ce03 | -21.61741 | -47.67936 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.7 |
| d3a9d721-7827-3a60-8178-f09a1deac3b7 | -21.61587 | -47.66906 | 2024-10-09 01:09:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 291e0e03-4704-3977-9690-1c2b722f468b | -21.61437 | -47.72218 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9353c085-f7a2-33ae-b6f6-088ac577ca13 | -21.61285 | -47.71201 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 315.5 |
| 6db569f2-2b69-3c32-a7a8-e6481825c889 | -21.61131 | -47.70176 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 817507a6-d99c-375d-aa10-5fdef13faac4 | -21.60977 | -47.69146 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 80c97037-1829-3bd9-9021-cac95278dbc4 | -21.60853 | -46.60754 | 2024-10-09 01:09:00 | TERRA_M-M | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| fb606ec1-5eec-3831-adae-bdf68803a891 | -21.60821 | -47.68106 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 1ad91444-2dcc-393d-bb1c-f075181594a2 | -21.60665 | -47.67067 | 2024-10-09 01:09:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4fa8a6ac-bdc7-3caa-a82b-e0a9c544615f | -21.60518 | -47.72385 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 85f515d7-def2-35c7-be4f-687e0dbb8696 | -21.60364 | -47.71359 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 62d6dce7-e11c-39a0-a39c-7acdd3e22af5 | -21.60211 | -47.70341 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 99ac26a2-d40c-33d0-9394-40544320702f | -21.60056 | -47.69308 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 235.8 |
| c7c5f2dc-e87f-35b1-b8bb-bae1e2c09bc5 | -21.599 | -47.68272 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7c69a323-1fcd-3143-9c66-c22c852f1d23 | -21.59602 | -47.7257 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 416055bd-f49d-39cb-85eb-541adf1bbf37 | -21.59448 | -47.71553 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7dfddc61-c037-324b-8af6-16bdb39c7d52 | -21.59292 | -47.70512 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2352a302-3cfb-3dac-b134-d1349a120f4b | -21.58547 | -46.98887 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 035bab53-c12f-3945-90da-27e9e2785532 | -21.58545 | -47.90525 | 2024-10-09 01:09:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5d9c99b1-450e-3078-b351-fc27def64953 | -21.58392 | -47.89511 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 28e86ff0-2147-3b9b-87a8-c2fdba6bc595 | -21.58381 | -46.97812 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 211762b9-52ac-3311-bdb2-558185c7a9c0 | -21.58238 | -47.88496 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 57c1a4ac-4fc4-32cc-afbf-bbb1f0057221 | -21.58085 | -47.87481 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 782c8a08-89ca-38ba-9dfb-680cf571b6a0 | -21.57784 | -47.91699 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2949d002-1ec1-319c-b248-3da84d73d072 | -21.57631 | -47.90686 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 40331c56-1bb1-3a5b-99aa-7b3f9931003d | -21.57597 | -46.99066 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 6c475ec8-76ff-3870-b420-b5e83335bc2c | -21.57478 | -47.89672 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| de1e0299-0500-3388-b2f3-15eacb05fe6d | -21.57429 | -46.97986 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 23787530-4914-3b5f-a25c-ac618616985b | -21.57324 | -47.88659 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6156b6df-d620-35aa-b66d-99d3fc70c280 | -21.57171 | -47.87645 | 2024-10-09 01:09:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ca540bf5-99a5-378e-98f9-6fcc154f9d44 | -21.56476 | -46.9815 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| fad14fbf-5ce9-3f4c-8578-a7d30d8177d5 | -21.56304 | -46.97044 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 615a1154-74cb-3260-8ebd-e1ec190604ec | -21.55526 | -46.98333 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 07d55588-8784-3729-8aca-7ff4db37cad6 | -21.55353 | -46.97226 | 2024-10-09 01:09:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| af81aea1-1852-3810-933d-c6996fe95b96 | -20.99936 | -43.06863 | 2024-10-09 01:09:00 | TERRA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 083c18ca-5a21-303f-aae0-a13b9eabea6e | -17.83974 | -53.76038 | 2024-10-09 01:11:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c8732e6b-ffd4-39ee-bf83-c838c646fb1a | -17.78536 | -53.73092 | 2024-10-09 01:11:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2264b19c-5c90-3465-a47f-a11920491669 | -17.75168 | -53.79005 | 2024-10-09 01:11:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f7d07645-3fcd-3657-821c-5e1f448f20e7 | -17.34396 | -55.02829 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 26.6 |
| b9b7c55b-3590-3c6f-865d-704cffb96020 | -17.34224 | -55.0141 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 6054a49a-61e5-3e44-97f3-152d374ee510 | -17.32972 | -55.00138 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| b23b7184-3da3-3028-9267-f3950412fc6e | -17.32565 | -55.05956 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| ceefe892-6c15-3bef-9542-660bf0ec47fc | -17.32058 | -55.01694 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| ae1a2748-e55f-3590-9bf5-42955ee182d8 | -17.3189 | -55.00278 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 61831f16-67b1-3428-a13e-7535cddceab5 | -17.31478 | -55.06096 | 2024-10-09 01:11:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| d1f634a7-877d-348d-953b-78723302f443 | -17.15497 | -57.45722 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| b57fdda5-f8d3-3b1c-88da-0cc6d4455663 | -17.15319 | -56.13733 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 7bf72f09-d5a8-31d0-bdb7-45c1fef67486 | -17.15263 | -57.43588 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 238.5 |
| 01aa4f59-8816-3a9e-86e7-044c66bd51db | -17.15209 | -56.83764 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| e1fc758d-1f28-34ff-a37b-edc41ca9a5ec | -17.1513 | -56.12043 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 97bfe1ab-de91-31b0-af15-ccd129d52a73 | -17.14999 | -56.81855 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| aaa95e41-d3ed-3bcc-8272-ab36ab26162f | -17.14173 | -56.8583 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 0c5eec0c-db31-34d7-85be-978f4dceff2e | -17.13964 | -56.83912 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| b10a979e-cb1c-3d72-8cef-fe6088898e82 | -17.1304 | -57.35292 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 5fe31321-6fc5-3be7-9f99-17f6dfd13418 | -17.12926 | -56.8598 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| a04dc899-10e3-3cca-b5e6-f78b6b25f13e | -17.12732 | -56.86544 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 7e7e2795-3757-3a6f-b872-04244201a05f | -17.12719 | -56.84062 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 4352d91d-719b-365c-be04-77f480ea0706 | -17.12652 | -57.4389 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.8 |
| da6d16e7-724b-37e3-b208-ef1b87e6350a | -17.1251 | -56.84626 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.2 |
| f604c8e6-f769-3cce-9674-b03e9cf3df87 | -17.11573 | -57.46177 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| f65685a5-dbb8-3b00-989b-ae682dec47d2 | -17.11346 | -57.44043 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 4af371c1-3c8d-36f2-85e1-4659390265f6 | -17.10432 | -56.86282 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.5 |
| b715779e-d455-330d-9547-6ca152c7a8d0 | -17.10041 | -57.44196 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 3773abde-7a01-397d-92fc-44de30fbcda6 | -17.0899 | -56.86987 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| b0e9ca30-e889-3c6b-9bf7-b8920c6985f9 | -17.08775 | -56.85069 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 68a8ad67-156f-342b-9946-a60a80163dbc | -17.08011 | -57.36533 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| e7e4b64a-21d7-3c83-b535-6343a4dfd6d0 | -17.07853 | -57.35899 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| f0b24994-e041-31f1-b8df-86e23346c53c | -17.0753 | -56.85221 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| dcbe8544-4d4f-3ed6-8191-b8f803c9102e | -17.06285 | -56.85369 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| cd552748-3f82-33c4-9ea2-f6b90724a020 | -17.02581 | -55.03007 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8595a809-c296-30c5-9999-7f2152f9fef9 | -16.95281 | -56.79628 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 65394022-c977-3ea2-a09d-722c5341587a | -16.95074 | -56.77745 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 8059e74c-914c-352f-b678-93c82a37d844 | -16.92218 | -55.81193 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| f5e0555a-1e5f-3dbf-8fc0-d15bbb54e7c8 | -16.91293 | -55.81952 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 59c6b942-78d4-3523-8d25-850151f59a9d | -16.91103 | -55.80363 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 3aaadc47-236e-3e6f-84ab-b0052414cf01 | -16.91074 | -55.81338 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| fd9d846f-6f70-3cdc-b3c4-752096227391 | -16.90913 | -55.78785 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |


[Clique aqui para ver as próximas entradas](README26.md)
