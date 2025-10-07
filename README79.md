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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda49d84-eca5-3fcb-bb62-06cde1ee273c | -20.05194 | -49.5439 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| d63868f6-63f6-31c0-9202-3280868aaa6c | -18.66201 | -48.17934 | 2025-10-07 04:40:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2a0f043a-f640-31c9-869a-4b1d8204e63d | -18.15802 | -53.39069 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09eedde7-afe9-389c-a4ae-230ef4bb4aa6 | -21.48264 | -46.71997 | 2025-10-07 04:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a64bd955-fd1b-32db-af59-8ca6501d3258 | -21.61225 | -43.99543 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d60d6084-54ac-3f6b-9165-45e0c34f412e | -18.11163 | -53.34288 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6225a114-a583-30e1-a365-8847ff77ac4f | -21.52063 | -45.59576 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9338a6ac-11bc-33b7-b39e-9d3b5fccbe0c | -22.90704 | -45.58882 | 2025-10-07 04:40:00 | NPP-375D | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7d38157-ef02-3b4a-904c-583f1104e5a8 | -21.51999 | -45.60152 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 1ef72bb2-9c42-3497-9e91-2ac65161fe6b | -18.96954 | -47.82904 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e1c944f1-4de0-3c3f-9733-b7d299def98e | -19.44678 | -46.46123 | 2025-10-07 04:40:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa993100-c558-3f78-bcc2-e0a649c13d8e | -18.23849 | -53.3623 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92676cef-19cb-3c53-bc8b-92d7f15c6ecd | -20.18715 | -45.41643 | 2025-10-07 04:40:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f56e7687-0d6d-3ef8-b2ad-75dfc38362dc | -18.15231 | -53.40263 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4d2d242-5658-3e14-919f-3068e7910a78 | -23.31663 | -45.7591 | 2025-10-07 04:40:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 831ae122-3305-369b-8249-2d49b0e38d73 | -18.11862 | -53.36548 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da839042-0938-376c-8251-ffdc61302cc7 | -18.96821 | -47.82645 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f984b85f-a1da-3093-8969-95c09f47c6ba | -21.90616 | -44.88472 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 65a470ff-000d-3334-b371-c4c1b9aaf61d | -18.16163 | -53.36967 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfe9d22e-867c-3edf-b34d-0a53d93c9248 | -20.06157 | -49.54945 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| bedb053b-e02a-3809-9986-e47602018e00 | -22.1785 | -49.38329 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e17adf7-ef02-34c9-abed-ec300608acd9 | -18.15459 | -53.36822 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc1e6ca7-85f2-3ce4-bace-15c129dba28e | -22.9456 | -49.29496 | 2025-10-07 04:40:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1615f795-3f2b-347e-b65c-50f02b592ee9 | -21.61723 | -45.29264 | 2025-10-07 04:40:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05cd1ae3-68a8-34cb-afeb-6579a3db66d2 | -19.58909 | -44.85343 | 2025-10-07 04:40:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ce99f08-d058-383e-a4fb-3b0f99c8138f | -18.27178 | -53.33809 | 2025-10-07 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a389ed8-e148-339a-a08a-aceed18e628e | -18.11728 | -53.35229 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 07956f24-0315-3ee9-b510-7e802d909da0 | -18.16442 | -53.37466 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 836b76a7-e090-3f6d-870f-f09be5933228 | -22.67344 | -49.19238 | 2025-10-07 04:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c1d7e89-4bfa-35a2-b102-744aebcf18c8 | -21.10101 | -44.20506 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f13be6d-f730-3ba0-afed-8e02623d2ca9 | -18.10364 | -53.36771 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a34e1ad7-363f-3188-97a4-6df45fc4a305 | -20.06214 | -49.5456 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| b3304245-8648-3a74-b478-b9c427aaf3f9 | -21.49388 | -46.02599 | 2025-10-07 04:40:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6aaa4bd9-dc6d-364c-bd5b-e3446e6497af | -22.15242 | -49.39156 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8c8f6d7-73a3-3e7a-8fd5-19af82578d02 | -20.74874 | -43.47295 | 2025-10-07 04:40:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b1169ecb-261d-3daf-b491-d0160861a3ae | -19.02368 | -44.73283 | 2025-10-07 04:40:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c746723-5ae5-3a2c-9e77-f44ca75bec9b | -21.51968 | -45.60383 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e378f1f7-a3e6-3699-8763-24946a87b0b5 | -21.60763 | -43.99451 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0bfdb147-3658-3830-baa1-4a664a0b08e8 | -22.58317 | -44.44529 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a79bd46c-3b1e-3a3d-a6a2-2a529cbd74f7 | -20.08246 | -49.59622 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| e8b9eedf-7da8-38c8-8dca-4c70a73c26c6 | -18.1087 | -53.35964 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a77693b-a8dc-3a54-b939-d06a0b01677d | -19.04137 | -48.13667 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c198b7d-ce0c-3b85-bb28-ff23f05e0d52 | -18.92857 | -49.48585 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c765ea6-b284-350f-a080-413aff2bf9d2 | -17.6808 | -52.24342 | 2025-10-07 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9204ae76-4add-310f-8c9c-3c7351239c59 | -23.19129 | -47.23513 | 2025-10-07 04:40:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6fcc5092-603a-3a3a-b78f-051eccedbf69 | -18.15523 | -53.3857 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63dbcbff-5f1c-3d3e-9a88-a7557d7eadef | -18.78059 | -44.61741 | 2025-10-07 04:40:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d0791409-8e4d-3ebd-9408-f8a9c887ba47 | -18.10796 | -53.36388 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f31a025-9e19-3e34-be03-2c1a33580cc5 | -22.15301 | -49.38749 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 637ad06e-b37e-33a5-b4dc-223467b32dbe | -19.70777 | -44.11943 | 2025-10-07 04:40:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d0223fe-d342-3e00-b67b-c8422628af2e | -18.16031 | -53.35617 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94000824-933c-35b5-b08c-821b55a56cd4 | -18.17353 | -53.38533 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 728d1b51-6338-30ce-9673-e858998c4784 | -22.22608 | -49.72495 | 2025-10-07 04:40:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 844f662a-7fc4-3a3b-b65e-261c94559b01 | -20.21305 | -43.91947 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19a4fd17-e943-3ae2-bb5f-14b281201f21 | -20.09513 | -44.20205 | 2025-10-07 04:40:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0b7b528d-4a18-3e6f-8178-b865a2ba072f | -20.11719 | -44.41523 | 2025-10-07 04:40:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 25bccd5b-1c51-38b3-be48-25c100bbbb2f | -19.0134 | -49.75359 | 2025-10-07 04:40:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8bf5c90-df31-3c44-af8b-23757a2a61c7 | -22.16172 | -49.37643 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3b5c01b-c0ef-3998-96a7-82180c9e3044 | -18.11227 | -53.3601 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ff8c498-576b-3b91-a9ee-3f9264a2bd98 | -22.16113 | -49.3805 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 930b1207-0503-38eb-ab9d-37c46c27f45e | -22.54781 | -44.98119 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9582e179-1364-3a77-bacb-2a1bdff0e7b9 | -18.1524 | -53.38095 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be8987ed-5b05-3e8c-8973-cd869bb11cd4 | -22.15648 | -49.38807 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9834bdb7-3409-39fe-99c6-4d0356e8c35f | -21.18674 | -45.67527 | 2025-10-07 04:40:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef6027fb-e2d6-3dde-a88e-d9de71c1be00 | -23.23646 | -46.71573 | 2025-10-07 04:40:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a095b459-0530-3c43-8cc9-48472adccec1 | -22.91009 | -45.58687 | 2025-10-07 04:40:00 | NPP-375D | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 567f5178-54ad-34f2-81f7-3949c277707c | -17.58485 | -52.42102 | 2025-10-07 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0d4e300-4b54-3c2c-a2dd-757e45670a2a | -23.18086 | -47.25473 | 2025-10-07 04:40:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e1b059d1-d50d-3dad-8ce3-fd80e46cb1bd | -20.05817 | -49.54889 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 2571914c-e050-381b-9201-a8e2cb8b12be | -18.15536 | -53.36377 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f1f98b7-1636-3d0a-991e-40e97942158e | -22.1646 | -49.38107 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34b5a8aa-9632-39fa-b311-c4d5d0329303 | -18.18202 | -53.37831 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8422d11f-4935-351f-930f-ed19b34728ec | -18.11654 | -53.35649 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 32eee1e8-a4d0-3f7e-b228-bab3ebcb03dc | -18.10733 | -53.3466 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 683d9f90-f277-340c-819a-a1df74d4f108 | -18.17779 | -53.38174 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52fa517e-d8a9-3890-b140-cbc5800a2a19 | -22.31775 | -42.5327 | 2025-10-07 04:40:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c2b21d72-e53d-3654-831d-69ead1589e32 | -23.37313 | -47.17144 | 2025-10-07 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42107fa1-c6cf-3dba-8015-a4a31fa776d9 | -18.10806 | -53.34246 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66530394-9f37-352e-9e36-768d1dfdfe8b | -18.17992 | -53.36928 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfa9ecbc-352a-38ff-9e01-7f4d6b357657 | -21.18976 | -45.67337 | 2025-10-07 04:40:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44bcef67-4e44-3011-90bd-9da5cb316bc2 | -18.92179 | -49.48478 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4132393b-1bb3-3d23-9d2a-d018b8d0e920 | -20.11279 | -44.41426 | 2025-10-07 04:40:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 53e516a8-6d37-3909-9d0d-40b8efaa15d2 | -20.5069 | -47.01194 | 2025-10-07 04:40:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd903bb0-b442-380a-9ffb-6a32a955dd35 | -21.07765 | -46.90316 | 2025-10-07 04:40:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16158b19-0c17-3ccf-a1ea-d33de4252b27 | -20.32143 | -45.11938 | 2025-10-07 04:40:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d59fa02c-506e-3220-baf3-a492258d82a6 | -22.22952 | -49.7255 | 2025-10-07 04:40:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 56d92ca1-173d-315a-937b-f3a08dcbfeed | -18.11935 | -53.36132 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6234498a-9dd7-3ee8-b25f-5e1be754fd70 | -18.18344 | -53.37002 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e65c3545-b3cf-34de-9e61-bd2a22fedc90 | -21.61941 | -43.99732 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4fbc1c1c-47b6-3a1f-aee4-85982b9acb06 | -19.66108 | -48.50046 | 2025-10-07 04:40:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0458c265-db69-31c7-a896-cac6adf88070 | -20.05477 | -49.54832 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| e34c9385-a66a-362f-b8f8-f42aa24e4cb5 | -19.0449 | -48.13725 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33fbaf97-6f64-3125-a92a-32179a3d5b36 | -21.74824 | -44.41494 | 2025-10-07 04:40:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b46a4842-d1c4-37a0-bbc7-03c53791c973 | -20.85187 | -49.48012 | 2025-10-07 04:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c97e6fe6-c2f4-31e3-8638-53ad0f4f237d | -20.1221 | -44.41196 | 2025-10-07 04:40:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 19e72491-6f8a-3ab9-a5af-bedf153e0dc1 | -20.0322 | -48.23956 | 2025-10-07 04:40:00 | NPP-375D | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc79fdab-f7b7-38d7-8109-2c4433df199e | -21.43175 | -46.68139 | 2025-10-07 04:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7d1cc601-2e48-3192-818a-e0951c92c27d | -22.16808 | -49.38164 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45aaaf10-f60e-360d-8446-1b9f1da5c708 | -20.58401 | -46.30692 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e373ce8-9a1a-3fac-8d8b-4a6ffc43a754 | -18.14188 | -53.37852 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README80.md)
