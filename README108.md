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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d20720-f522-3253-bc62-7470889483aa | -22.96074 | -45.95594 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3834ac05-ceba-315a-832e-0244b93300b0 | -22.9561 | -45.95598 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b3e21c33-1875-3429-ae19-971da4bf99a3 | -22.95537 | -45.96283 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 73713f64-c371-357f-a52d-b953ab1387ef | -22.33901 | -47.75821 | 2024-09-27 04:44:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fcb61025-1e19-34e8-b7ef-4600ccd749d7 | -21.47955 | -48.08751 | 2024-09-27 04:44:00 | NOAA-21 | MOTUCA | SÃO PAULO | Brasil | 3532058 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 614feb1f-892c-3cf6-8b9c-c8b7ac32be26 | -21.4795 | -48.08938 | 2024-09-27 04:44:00 | NOAA-21 | MOTUCA | SÃO PAULO | Brasil | 3532058 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eb2c5a6-853f-383c-aff0-d6ee35442cff | -20.80737 | -48.93471 | 2024-09-27 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c85ea01f-a77d-30bb-a810-f73032f8374c | -21.5118 | -48.63239 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f4a920b4-6668-3110-83f1-d16eeda6ce37 | -21.51172 | -48.62884 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3283d09b-4d43-3401-a4db-bdcab61d2e1a | -21.51113 | -48.63738 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24295a78-b48b-31d2-9ec4-1aeee829bcfc | -21.51109 | -48.63386 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c059f610-778a-3e22-b5b0-8de3696bb1f5 | -21.51046 | -48.63884 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf25647b-d4f0-33af-af04-21df11493fca | -21.50801 | -48.63178 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b5cce8a1-a001-3592-81c4-2417d80504be | -21.50793 | -48.62823 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b25bb1d6-21b1-32ac-9466-27851b2a303a | -21.50734 | -48.63678 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 979658bf-a328-3844-a97b-2ace8f89090b | -21.5073 | -48.63325 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0623f28d-9572-30fc-9618-989bf6875f52 | -21.50666 | -48.63824 | 2024-09-27 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede1d4de-d087-3390-b771-619f5768f0dd | -21.27676 | -49.45705 | 2024-09-27 04:44:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 0ad43546-6f69-3042-af50-4ccf17ea52a9 | -21.26197 | -49.20922 | 2024-09-27 04:44:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 816aa570-0b38-3874-b0cd-7c46e84e11f9 | -21.10466 | -49.13383 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f1192cb-a570-3abd-9fe4-5a4bf53447c1 | -21.10036 | -49.13786 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 57ddc0fa-117f-304c-a454-d5162f97f553 | -21.09973 | -49.14244 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ebd0717c-4fa8-3d10-9c9b-6fffe840aa1d | -21.0973 | -49.13276 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 798e5e3d-6d3f-36fd-9d22-bb7587b93d27 | -21.09668 | -49.13731 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fee0d884-c30d-37fd-b400-1ae62ca26a7a | -21.09606 | -49.14187 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6d1b7bbd-ff4d-3452-a012-7636a2ba45bb | -21.09361 | -49.13225 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| aab235a5-ac84-34a8-b76b-c2e33be2ed9d | -21.09299 | -49.13681 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 01d8f0a0-e85a-3621-b987-4d9219847876 | -21.09237 | -49.14135 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d0a6b076-53da-3785-b099-63084c6b988d | -21.09176 | -49.1459 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 90feefc5-c200-33af-806a-1e8ea71248dd | -21.08992 | -49.13177 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4cb46ee5-2522-3c26-8007-56a0d2f297e9 | -21.08931 | -49.13633 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 893aeeff-e035-357a-94f6-597c3079b231 | -21.08869 | -49.14085 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7a207e8c-b1a7-3bcb-886b-e61ba944e05a | -21.08808 | -49.14536 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4922ccbe-ee50-33b1-83b6-6849341349e0 | -21.08501 | -49.14035 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10fcf87e-b767-3732-9fe3-8cfd636b1a2e | -21.0844 | -49.14486 | 2024-09-27 04:44:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b516ee29-3e83-3609-8ced-71eb363d11db | -20.6507 | -49.93452 | 2024-09-27 04:44:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c16cd64-9422-3119-8759-6a4d28f0a6fc | -20.64717 | -49.93395 | 2024-09-27 04:44:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d9f474e-62a4-3769-a118-8d855fb2de8b | -20.64659 | -49.93814 | 2024-09-27 04:44:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 06bf741a-a3f5-39c6-82ac-0b49297b69ab | -20.64365 | -49.93338 | 2024-09-27 04:44:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fde2649-cd1d-35b1-bef7-afcdcd9c33b6 | -20.64306 | -49.93757 | 2024-09-27 04:44:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59c04cfc-1f2e-34b6-b513-d3735641b12d | -25.78535 | -53.03184 | 2024-09-27 04:44:00 | NOAA-21 | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31211e15-4d42-36b0-854a-47a2c3927366 | -19.88363 | -53.38758 | 2024-09-27 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e52768f-acbf-306a-b1ff-2410ae5cf2df | -8.1983 | -64.0785 | 2024-09-27 04:45:53 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e0b405f9-3baf-376b-8499-4568c82eb4f6 | -22.87744 | -42.47767 | 2024-09-27 04:46:00 | AQUA_M-M | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| a0d30bfc-7b46-30d9-bb6d-776be4abb344 | -22.67631 | -42.85192 | 2024-09-27 04:46:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 8d983407-100f-3e14-8403-97985f3e512d | -22.67457 | -42.86251 | 2024-09-27 04:46:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f0cd870f-f9fc-3b14-ad71-ec2478c198bc | -22.55573 | -43.8134 | 2024-09-27 04:46:00 | AQUA_M-M | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 3c37c4db-ee47-38a1-af21-8cbdfa0908b6 | -22.34885 | -43.5141 | 2024-09-27 04:46:00 | AQUA_M-M | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f31fbfe6-4749-3dd0-b6d5-a879d0e4ea0e | -22.3384 | -47.74112 | 2024-09-27 04:46:00 | AQUA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d5111902-144f-3b03-8be7-23da6974db17 | -22.33492 | -47.74738 | 2024-09-27 04:46:00 | AQUA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8df42601-574d-3b99-9c8c-660d7ce3ea62 | -22.33439 | -47.76212 | 2024-09-27 04:46:00 | AQUA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5adf4978-ac65-3174-884e-41cb83e4f819 | -21.964 | -45.80937 | 2024-09-27 04:46:00 | AQUA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| b6398005-a1d9-33c4-b966-3c728889674d | -21.96394 | -45.81891 | 2024-09-27 04:46:00 | AQUA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| aa5ec96c-bd5b-356a-a9a4-394834292b0d | -21.41054 | -42.96866 | 2024-09-27 04:46:00 | AQUA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| 857d17cb-7b92-37b9-b17e-c0800a5dc29f | -21.3917 | -42.96434 | 2024-09-27 04:46:00 | AQUA_M-M | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| d816658b-7c41-3e8d-bdde-142d26ba16d3 | -20.6234 | -42.89725 | 2024-09-27 04:46:00 | AQUA_M-M | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c2c2c171-9d1a-307b-9aee-0ed25fd9cf83 | -20.59674 | -41.22973 | 2024-09-27 04:46:00 | AQUA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a5058a61-267e-3118-84c8-a4a4ad979225 | -20.58776 | -41.22828 | 2024-09-27 04:46:00 | AQUA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 55765933-87f1-3d1b-9681-c2d70217dd93 | -20.51938 | -41.95869 | 2024-09-27 04:46:00 | AQUA_M-M | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 766a1be3-ff09-3192-9396-9b60354714b2 | -20.51774 | -41.96887 | 2024-09-27 04:46:00 | AQUA_M-M | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| 6d2515b1-6537-3ec0-aad7-77e5826efba3 | -20.51022 | -41.95704 | 2024-09-27 04:46:00 | AQUA_M-M | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 8c95d0d9-2f4e-322d-bbc6-c6db7155d63e | -20.50861 | -41.96709 | 2024-09-27 04:46:00 | AQUA_M-M | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 733fd982-64b7-36b0-bdf2-ed3d045bd5b6 | -20.49258 | -43.49021 | 2024-09-27 04:46:00 | AQUA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 92a7ede5-99ab-31ee-8090-d7f7d632d768 | -20.17007 | -43.50947 | 2024-09-27 04:46:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 49075842-a47e-37b0-9694-3bb5f7997a7d | -20.16817 | -43.52067 | 2024-09-27 04:46:00 | AQUA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| ebf886de-a68e-399e-9f00-9fd46a24cc6b | -20.16634 | -43.53141 | 2024-09-27 04:46:00 | AQUA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.9 |
| e5006c6e-7efd-38e7-b356-b937f66a2297 | -20.15479 | -44.3287 | 2024-09-27 04:46:00 | AQUA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 052f6767-2c3e-3c72-bd77-defc6b88a93d | -20.1523 | -43.55347 | 2024-09-27 04:46:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d30eb7c5-43a8-38ec-bddf-953fa3636c27 | -20.15027 | -43.50523 | 2024-09-27 04:46:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| be4f9ebd-b6c5-3ac0-a7ab-cdf68884b971 | -20.14829 | -43.51678 | 2024-09-27 04:46:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| b55e0f39-3833-318a-9b4e-a887ae5983c4 | -20.12067 | -43.44013 | 2024-09-27 04:46:00 | AQUA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 1be6dd86-e5fd-361e-a684-90d521c6becc | -19.94598 | -43.79889 | 2024-09-27 04:46:00 | AQUA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| af857e36-89e2-3112-9078-6274a583b23b | -19.8681 | -42.1576 | 2024-09-27 04:46:00 | AQUA_M-M | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d7f861b0-06a7-3f42-8794-8ea04c210c47 | -19.71072 | -42.3841 | 2024-09-27 04:46:00 | AQUA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| de3a957f-6adb-3eff-9743-03387b36d10b | -19.65261 | -42.857 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d062afb2-bb29-3579-b2f7-67986580ad96 | -19.63194 | -42.92154 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 20aea288-6f03-31ee-8d58-3905a90df0c7 | -19.6311 | -42.80701 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 3073d026-2e69-3d6b-8057-36e4673b8885 | -19.63015 | -42.93233 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 23003c32-4f94-39ac-bd89-ea957536f611 | -19.62443 | -45.86485 | 2024-09-27 04:46:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9b22957f-2408-3d90-9cd1-7d99e0366ca5 | -19.62124 | -45.88193 | 2024-09-27 04:46:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 78c53c3e-b1db-3a4c-ad4e-defe85720565 | -19.61979 | -42.81535 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 4cde5df7-dc84-321a-8789-078eaed09a26 | -19.61813 | -45.85839 | 2024-09-27 04:46:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a9b330a4-e346-3e8d-ac10-4c7720e1da35 | -19.6179 | -42.82661 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| c0497541-2c5f-3c36-978b-9ef5cbf9e421 | -19.61502 | -45.87563 | 2024-09-27 04:46:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 5c05b900-0957-310f-9530-2046c003826b | -19.6119 | -42.80314 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| f89a2956-a58d-358a-b4e7-71c0848865a2 | -19.61009 | -42.81394 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 3165254c-f992-32ed-9fc5-db4a62d037b4 | -19.60888 | -42.7975 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 8cad63d0-ded4-35de-84c7-9296a9fd9a63 | -19.60823 | -42.82505 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| abd99446-a5b3-3db6-9142-73406a0eab6a | -19.60713 | -42.8082 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| 78935f11-bc6d-329e-be2f-05515697a58c | -19.60535 | -42.81914 | 2024-09-27 04:46:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| 8152a296-be66-312a-b71d-5bc8820ba78f | -19.60004 | -46.96709 | 2024-09-27 04:46:00 | AQUA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 98783b95-01ef-3c2b-b3ca-1fd39253ca5a | -19.59896 | -46.97212 | 2024-09-27 04:46:00 | AQUA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f8a94f3e-0ecb-351c-abaa-0580bd7d02df | -19.58538 | -46.10872 | 2024-09-27 04:46:00 | AQUA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f74b7a7a-713f-3ab9-858b-314dc0ee9eee | -19.57792 | -46.11254 | 2024-09-27 04:46:00 | AQUA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9ce244af-8a04-35ca-aa10-27b8617b388c | -19.56768 | -42.687 | 2024-09-27 04:46:00 | AQUA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 81f683c6-8d41-38bd-b211-cb54b6273bc3 | -19.56591 | -42.69764 | 2024-09-27 04:46:00 | AQUA_M-M | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 96616469-75df-3272-8a81-1c5399a41337 | -19.39322 | -42.56376 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 9d3f948d-77d6-335a-85bc-8638b28fa76c | -19.39146 | -42.57438 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| ccc771b8-2369-3b40-ad40-e2db326cd04f | -19.38975 | -42.58473 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 56547120-578d-37cc-95f5-ad79bc402d6f | -19.38364 | -42.5623 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


[Clique aqui para ver as próximas entradas](README109.md)
