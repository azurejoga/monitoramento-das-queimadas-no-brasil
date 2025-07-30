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
| 8b82ecd2-0e48-37bf-98e6-0329259655c6 | -9.45566 | -57.85008 | 2025-07-30 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71bbe151-2800-3b10-ab12-e51c7eae345d | -12.61956 | -48.06135 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d3d76fb-01e2-36ef-8ba3-992e5262ebde | -11.80979 | -44.26769 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0918600f-09f4-3d02-b884-780426fee693 | -9.45972 | -57.84939 | 2025-07-30 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5eddeac-f232-39df-b493-6802d3457366 | -11.54084 | -44.24904 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 718841a1-21c8-3745-9234-18d3ffd4f710 | -11.99348 | -46.92741 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 578dbc21-165d-3057-b952-743730916995 | -9.45378 | -57.84824 | 2025-07-30 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c6d25e-c13d-32a9-af92-d00ab9ed913e | -12.81431 | -43.09752 | 2025-07-30 04:29:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4ae5bba1-b806-3dca-addd-b7bfbff2c1f2 | -11.33778 | -51.24774 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4fecf2f-3621-3242-b3ba-c70cf18dc275 | -11.81889 | -44.25608 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ed057e3-de86-31aa-8e84-c642db659d0e | -11.98048 | -46.68128 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 786f8264-7c79-3ccb-b491-59de5c970aa7 | -11.4584 | -45.1126 | 2025-07-30 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| addd4341-7d62-38eb-a19f-7babdd8b68d0 | -8.5211 | -43.3063 | 2025-07-30 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| cb3ef7d3-2fe4-3f52-be52-2d35ef7ec0f6 | -10.6172 | -45.2282 | 2025-07-30 04:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 074f393b-6932-3a3a-9db9-8525e522c754 | -6.526 | -56.1923 | 2025-07-30 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f842a155-a834-3592-b31a-18212258bee8 | -10.6169 | -45.2512 | 2025-07-30 04:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ae2f7cbe-332c-3c45-b4e6-97522bc42745 | -23.60501 | -45.36785 | 2025-07-30 04:32:00 | NPP-375D | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e0a7739d-9bce-31c1-b8b0-9493f977b9e1 | -18.4118 | -44.1877 | 2025-07-30 04:32:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f6420a-41c0-33bf-9755-e8d7920ad274 | -18.73754 | -47.5348 | 2025-07-30 04:32:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21878e67-7003-383b-be7a-4c4666b2c4a9 | -21.04626 | -55.98473 | 2025-07-30 04:32:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dfea439-a007-39ae-b371-24035e94c44b | -17.58303 | -47.49503 | 2025-07-30 04:32:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cc36374-4856-3f2b-bd8d-bfee51033f9b | -19.40183 | -46.52219 | 2025-07-30 04:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f96b902f-1af5-39d9-8591-94a6f1a1eb7b | -18.77984 | -47.62373 | 2025-07-30 04:32:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b7eb598-07be-31c3-8995-6f5f55d63d07 | -19.10147 | -44.40809 | 2025-07-30 04:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db855980-3b04-3991-bc3c-eb6aec94e782 | -18.5676 | -44.42013 | 2025-07-30 04:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 823a7a80-d779-342f-a3b1-034acbddff71 | -19.99314 | -42.22614 | 2025-07-30 04:32:00 | NPP-375D | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c4f653b-e395-32e4-9d33-0651a48a1921 | -17.5866 | -52.42158 | 2025-07-30 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc9c31b2-b6d3-33cc-8f1b-629103131da7 | -21.39302 | -48.67462 | 2025-07-30 04:32:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad843ee-2aae-325e-91c6-9ab7f49c1bd9 | -17.48298 | -46.73793 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 82dec4eb-6d56-3d86-b3bc-bd029fc4941b | -17.87609 | -48.10672 | 2025-07-30 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b752e247-7a5d-3830-931e-2cf89fa861cb | -21.33012 | -55.64088 | 2025-07-30 04:32:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41c19c6a-4541-3b0b-9bbf-b57b2fe3cafa | -19.10636 | -46.57647 | 2025-07-30 04:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f234e1c-a923-3fd3-bb24-688b68966520 | -23.00495 | -48.63443 | 2025-07-30 04:32:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1c23b5d-0615-353f-b77d-3d2edba8627f | -17.48987 | -46.73905 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c0cf0e6-f523-314e-b1fb-1aaff117b6fd | -21.39359 | -48.67083 | 2025-07-30 04:32:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e46cd128-ef80-3966-b6bf-c873dd328be9 | -17.49044 | -46.73514 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7aeabc3-cff1-3d7b-8cc6-f1fb27d449f2 | -19.75646 | -43.13041 | 2025-07-30 04:32:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 18eece5d-f3cf-304d-a2a5-98ab78210a78 | -21.37933 | -56.0966 | 2025-07-30 04:32:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e9aede3-ed2f-3a14-9d2d-7d178d532d29 | -22.23874 | -47.05608 | 2025-07-30 04:32:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5db91d4a-0c8f-3c36-b5fa-c47ea47b1dd1 | -16.63648 | -49.35226 | 2025-07-30 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b108e2-3542-3c66-8433-d78959cfbda6 | -17.48642 | -46.73849 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3bbf33fe-647e-399d-985a-65c92239ddf5 | -20.29169 | -54.0744 | 2025-07-30 04:32:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39977144-7677-3e46-aa7b-198ecc7d97f7 | -21.32251 | -48.69817 | 2025-07-30 04:32:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 75a22b40-7d4c-31cd-9888-10bd3610d1f7 | -21.38128 | -56.09871 | 2025-07-30 04:32:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d0b3477-98ac-30cf-b960-71c06f1e70eb | -19.74388 | -42.10302 | 2025-07-30 04:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3516b0e0-7974-34e1-acaa-141cd460b71d | -21.33583 | -55.63366 | 2025-07-30 04:32:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de7cd2a4-bdd4-3a42-b212-21ee9ff04444 | -17.87665 | -48.10305 | 2025-07-30 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b65f290-36e0-3f00-aaf8-94f23e45b011 | -19.1649 | -46.59423 | 2025-07-30 04:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e353e8-60ee-3b42-9ee6-a122c52d7666 | -22.99614 | -43.58372 | 2025-07-30 04:32:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de29b2e4-e704-3a95-a3be-0999cc6abb55 | -18.77645 | -47.62318 | 2025-07-30 04:32:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aff17e21-74bf-3960-8578-38f939d1c5ef | -20.29618 | -50.95687 | 2025-07-30 04:32:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9caf20fe-fcd5-3aa8-9bf7-dc6d1327717e | -22.99425 | -49.78326 | 2025-07-30 04:32:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 27090a33-9dc9-3ccc-b6b8-082c5408de97 | -20.45753 | -45.54943 | 2025-07-30 04:32:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd85e332-5334-3ace-bad0-7ed6accdca3e | -21.33504 | -55.63779 | 2025-07-30 04:32:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef62e6b-43e5-3918-af39-9df5f6405aee | -17.487 | -46.73458 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 95f373f1-6f8f-3621-b100-1650fbb2098a | -16.83093 | -49.2439 | 2025-07-30 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30d6a451-40e1-32b8-a5ab-8fe4ff52d24f | -16.78518 | -49.33666 | 2025-07-30 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 968a35ac-b7bc-34e3-a936-9390958a3e7b | -17.48355 | -46.73402 | 2025-07-30 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59aecac1-df13-3213-b7ac-6b8b225daab2 | -17.98014 | -45.6049 | 2025-07-30 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb360c0b-2a31-3c52-922d-7577ccba89fe | -16.62357 | -49.53766 | 2025-07-30 04:32:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea1d6d54-e041-3bca-a43a-d46f04baba37 | -20.47688 | -53.67765 | 2025-07-30 04:32:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84b15ea6-9a9c-335d-ad4e-1dd058f249ae | -18.56301 | -54.76098 | 2025-07-30 04:32:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b44c0fb-e960-39e4-85c4-595dbc2c7611 | -22.91666 | -45.37995 | 2025-07-30 04:32:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8e17783d-097f-38bd-b43f-83cd15fb862a | -17.62304 | -53.85994 | 2025-07-30 04:32:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ec18935-18f3-3065-9aa2-dcd78738e34d | -21.98688 | -46.8213 | 2025-07-30 04:32:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92c147c8-0b55-3149-a03d-7348873da5b7 | -21.32979 | -48.69553 | 2025-07-30 04:32:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 21d71d3c-e328-3298-a45b-70d8b44c8e79 | -17.98076 | -45.60051 | 2025-07-30 04:32:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ffd922b-bc4a-3444-b365-0abbb2d7dde6 | -18.56373 | -54.75716 | 2025-07-30 04:32:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c69593ef-46c0-3add-bc12-31ef1f26966f | -22.99668 | -43.57912 | 2025-07-30 04:32:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f2f6128a-2027-36f7-a42c-6aa7bc6088bf | -18.17974 | -46.99581 | 2025-07-30 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55ec7af6-2cc6-3b35-8dd7-887d24e318ab | -16.89087 | -49.07504 | 2025-07-30 04:32:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8a352d8-520a-328e-8ee1-45f0eb6ae1a6 | -17.97651 | -45.60434 | 2025-07-30 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 582e6d14-1703-39db-8cf9-1f762fc13264 | -19.74436 | -42.099 | 2025-07-30 04:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9eb5d939-674d-3d5e-a2b3-66393046fc79 | -6.526 | -56.1923 | 2025-07-30 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f27ad031-d26e-3f5d-a4c4-7e8a524a44e6 | -10.6172 | -45.2282 | 2025-07-30 04:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 4cacbf17-7fef-30bc-935e-f088c276c56b | -8.5211 | -43.3063 | 2025-07-30 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e8e69e5d-08a0-3b2d-9ebc-8024b82c2736 | -10.6169 | -45.2512 | 2025-07-30 04:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4eb884bc-626b-36b0-8419-f8b32fcc97ea | -4.64667 | -43.12862 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ae7bbd-f994-3793-a5b2-2c3719429d73 | -4.59756 | -43.31205 | 2025-07-30 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6275c9a2-fe12-3d6d-a994-31bc81f55094 | -3.08317 | -52.92385 | 2025-07-30 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f157002e-4749-33af-8dbc-128017ea0820 | -3.91066 | -53.85219 | 2025-07-30 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d293c53-3f27-3a5f-bd72-c69ae56974de | -6.3911 | -53.36471 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e35bbe4-7f16-3fed-8079-97e7e0985eae | -6.69533 | -42.04789 | 2025-07-30 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7dfe6e29-14df-319e-91c8-cfff19756d67 | -5.8236 | -46.35143 | 2025-07-30 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b35d5db0-ce18-3487-9ce9-fa7515f6e8c0 | -6.03421 | -47.54973 | 2025-07-30 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7317a440-8d5e-327a-9c55-4a116c47ee4f | -2.80882 | -48.6623 | 2025-07-30 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0322b630-1649-331b-8651-6489426f33a4 | -6.39055 | -53.32541 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a84d23f-08a6-3dbd-8362-157ea3dd0aa3 | -6.88937 | -44.731 | 2025-07-30 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 183e8263-acb6-39d3-a0c1-16ee5cc7b04e | -4.65566 | -43.12559 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54ce1395-4852-3788-8dea-1d73071d9d6b | -2.91083 | -48.23959 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7fb8fa8-2052-3494-8377-0f90a3d13e7d | -7.1032 | -44.37715 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc4fe56d-3cb8-3068-808f-9b5eafbf6f91 | -4.58448 | -48.01798 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7856130c-2d13-3563-8166-d01bc87a824a | -4.86013 | -43.23172 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5a919d4-05bb-353e-b0ae-c0123cb17a85 | -4.10086 | -48.19963 | 2025-07-30 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2c8c464-afb6-31da-b543-28dbc92cbe46 | -2.90436 | -48.24503 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ed38eaa-8b9f-32f2-bdbb-779d5a597edc | -3.88628 | -41.03226 | 2025-07-30 04:49:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bcff54aa-fe30-3fb0-954c-e20863cb01df | -3.30103 | -49.19223 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c44a7cc1-56bb-3af0-b106-3a9de8a67fd9 | -3.66481 | -51.23854 | 2025-07-30 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b5d2fef-0268-34f0-b638-6b791b7f9ee0 | -6.03016 | -47.54913 | 2025-07-30 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7945edd1-2fe8-3af8-9453-c19d33f04b22 | -6.45343 | -53.3568 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
