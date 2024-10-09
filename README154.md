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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e066f836-1c9a-3f41-8554-4cf0137279c1 | -20.79272 | -47.20525 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 928ad7dd-088e-3cf2-8496-357b4ba18194 | -20.79223 | -47.20924 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 785c717f-541b-3684-a2e2-7d0468f751b9 | -20.79158 | -47.24816 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ffa2e21-1ab7-36f4-b813-21c4da0eb8af | -20.79115 | -47.25161 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c47282b1-481c-359c-815b-756631d8398b | -20.79081 | -47.22076 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d93b30b-d053-3a4d-a3db-53d5b8c2dd03 | -20.79072 | -47.25509 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3ba48588-6dd4-35fa-9db0-aaa55e2e18d7 | -20.78964 | -47.19636 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e876c89-a058-39d3-b5e1-45256a0f8432 | -20.78942 | -47.23203 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d422a29-354b-331f-abcc-8965e12dc84a | -20.78892 | -47.23608 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73e7ee87-cb55-34a0-beae-cb69d0277282 | -20.78843 | -47.24006 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ec0d655-f38e-3ee4-bcfb-0ee30eec8966 | -20.78767 | -47.2125 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 321e5198-ca9e-3864-a9be-82fdd40bfed3 | -20.7872 | -47.21623 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0feb6469-15da-3226-b746-e74fab783c4c | -20.78707 | -47.25108 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4b9b262c-81ad-3653-b4ba-092bc90dbd90 | -20.78664 | -47.25455 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b4c0d55-739e-3188-91dd-b8c90851ff19 | -20.7844 | -47.23901 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1aaf7f3-3b24-37ff-9d57-d5f83f8dbf63 | -20.78392 | -47.24287 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57eabc7d-ef5b-3cb4-9fee-669fa210f18d | -20.7836 | -47.21166 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 349c64d5-9ca6-3ef3-be8c-d132682260e1 | -20.78346 | -47.24662 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b8ec9d7-baef-3bef-abb8-5c4f544b226b | -20.78314 | -47.2154 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3d9fd38-8917-3341-b661-58c42e3ae5d7 | -20.78302 | -47.2502 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b090c8c-141a-35a4-bc06-373101836449 | -20.78258 | -47.25379 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 94ff0d73-f4ff-3f5a-8cd5-6e2e2d30a715 | -20.78213 | -47.25741 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8904fdd-6473-34ff-b5ce-93eeb5bbb38f | -20.77954 | -47.21083 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1201c65a-2a47-3f5b-87a6-7a9db211b789 | -20.77945 | -47.24548 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| effdf418-12b0-3b03-8192-514d0680d62d | -20.77852 | -47.25297 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcc60210-af00-31aa-b07c-eabc13e0d34e | -20.6771 | -47.17654 | 2024-10-09 04:42:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ac6980f-d940-306d-ad59-9f5574e63191 | -20.67001 | -45.89194 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45ae4b95-5729-33b8-a832-e8589285981f | -20.66946 | -45.89657 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34016e75-9506-381d-889d-1c9c39931132 | -20.66892 | -45.90108 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81db21f6-5b14-3e16-ac97-7e6ef5686862 | -20.66492 | -45.89675 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 214a7763-1c03-3880-88cd-3e975e5fab41 | -20.66439 | -45.90126 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f9ea957-2bc8-3d27-bdb8-4c30612c9e61 | -20.66386 | -45.90576 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e3718b8-4956-3cf1-864b-60f7161b2798 | -20.66333 | -45.91024 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 243da1f9-3f27-339a-b970-79f9ee4c3918 | -20.66282 | -45.91458 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 066658c4-8a82-398d-b514-906932dd4416 | -20.65988 | -45.90127 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2b7b7f7-dfa8-3f82-bb33-d10b2846445d | -20.65594 | -45.89645 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 138c6dec-7b83-3deb-8666-7e7011e4d31d | -20.65539 | -45.90111 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed353fb5-fd0d-3d2a-a2a7-11b3bba3ad8e | -20.65201 | -45.89147 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddabad53-2996-38b7-b279-33c0db10aa5f | -20.65149 | -45.89588 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 568ecafc-3dad-3506-bb75-99a1868281d2 | -20.65096 | -45.90041 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 861be7e1-feab-38d6-b83c-766d42ada060 | -20.64753 | -45.89113 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 773c6769-5027-34fe-a610-9706977de002 | -20.64705 | -45.89524 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 274cb6b4-98ee-33ee-ba9f-011637ae76a3 | -20.64342 | -45.92621 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4daa7d7a-a755-3268-875c-e5fcc9cc3bc2 | -20.63999 | -45.91707 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd303fca-b913-3859-87f8-e27af4193f73 | -20.63952 | -45.9211 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a78d02c6-f9f7-3013-ab38-e808c6cfcec0 | -20.63902 | -45.92534 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 640bd349-ae2c-3a24-be4e-06fa8ba95d77 | -20.63851 | -45.92971 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc0bc16d-31fb-369a-805b-56bb1e8e13e7 | -20.63798 | -45.93427 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 187b8489-ba20-309c-94af-aac20f64e478 | -20.63608 | -45.912 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc3de00b-ca1a-357f-8a3e-31b3a6ebc959 | -20.63558 | -45.91622 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1afc067e-bce3-3c09-a90d-77b11e9accab | -20.63511 | -45.92031 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51c90712-67ac-3c96-98d2-5c7ce40ac5d7 | -20.63461 | -45.92453 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21137a00-7524-3fee-8411-a64e1afc5a4d | -20.63411 | -45.92884 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9a5491c-e8f9-366c-8489-4b344d447df3 | -20.63356 | -45.93355 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca918d7b-0f39-3bd1-8563-1b45a43beed3 | -20.63302 | -45.93821 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16c507a6-980a-373f-b1ea-4295374c202d | -20.63168 | -45.91103 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b32e470-7618-35a7-a024-4a580b8dad46 | -20.63118 | -45.91537 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c9e4de4e-b078-37cd-8f8e-f40858044a1c | -20.63068 | -45.91961 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c998bea9-ee34-3790-8c2c-2018cf90f92b | -20.6302 | -45.9238 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ec8609a-8903-3b7f-b4c4-ea8667d6e168 | -20.62676 | -45.91457 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a45e125-9f75-396c-9a8a-a199fb114ef1 | -20.36034 | -46.36491 | 2024-10-09 04:42:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaf1a9fe-c8bb-3ffa-99f7-1d89bbaac7e3 | -20.32185 | -46.15998 | 2024-10-09 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51b3869d-6997-3bf4-af96-b8e19e51f7e9 | -20.23029 | -47.32671 | 2024-10-09 04:42:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e85b4a2-9615-3999-8a1e-50b040f56456 | -20.22979 | -47.33074 | 2024-10-09 04:42:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1c6316f-644b-3eb8-8254-cfc521cf5c36 | -20.22573 | -47.33041 | 2024-10-09 04:42:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d30e15af-0fd5-30a6-93ba-15ad3499baaf | -19.9718 | -46.71095 | 2024-10-09 04:42:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77621d38-4913-3e48-8b45-4d91b5a95380 | -19.74875 | -46.64747 | 2024-10-09 04:42:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a431d19-d064-33d6-a811-98972f9e3c75 | -19.66351 | -46.22946 | 2024-10-09 04:42:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c96bd3f-6ef8-3cf1-9723-ff1ee5c50275 | -19.663 | -46.23359 | 2024-10-09 04:42:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d97135e7-bb39-3ebe-8666-d54934eaf731 | -19.64192 | -46.86023 | 2024-10-09 04:42:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e8ddd6-81da-3214-be1a-74f10bd46d37 | -18.9936 | -46.65633 | 2024-10-09 04:42:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6607d746-f785-33ea-aef7-f4c498ddfdc4 | -18.9931 | -46.66018 | 2024-10-09 04:42:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9e7e0a79-1440-3f27-8552-cece01051ca6 | -18.98947 | -46.65572 | 2024-10-09 04:42:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e81b4d96-2b08-3dc3-bf95-af88423f2dc8 | -18.98897 | -46.65959 | 2024-10-09 04:42:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e1aa7064-5f07-376f-b83e-5d3ec41a7f91 | -22.19914 | -48.11098 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5e54dce-0d74-3a37-99b0-4e49cf4fd1f3 | -22.19306 | -48.15907 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27e40ea8-8ed9-3e3a-b05a-f08196735ddd | -22.18912 | -48.15851 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 771cca1d-064c-336e-88d3-62a3de9c0f30 | -22.18518 | -48.15798 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ce729b9-f59b-3ae3-89c9-839a1ac52157 | -22.18451 | -48.16324 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 368af6ff-df61-3a29-a295-91178fa19970 | -22.18057 | -48.16274 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfdff4f0-88c3-3ac0-ab0c-ed781a7214f6 | -22.17597 | -48.16747 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a095c40e-aec1-3893-9773-98d791787662 | -22.15305 | -48.12621 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73168479-781a-3be2-8045-4e3df2881ffc | -22.15006 | -48.13007 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0eaa24da-9ca2-35eb-b285-09b08a98152b | -22.14979 | -48.08753 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cce29f71-6246-38bb-ac65-fe133c543c7d | -22.14912 | -48.12553 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e808639a-6a91-3fba-81fe-a2139b511d6b | -22.14771 | -48.08627 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c75db10-9c9c-379d-b7b3-9a03f0a3beee | -22.14613 | -48.12941 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75e18f4b-b2c4-3db0-a617-118186caf714 | -22.14583 | -48.08702 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c00373d3-66de-39a8-aea3-24460d1e4a7a | -22.14454 | -48.13015 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fee121e-cf82-3a86-9673-6d9169983116 | -22.14357 | -48.11818 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c0436d3-b9ca-3aec-b0c0-b95fd029fc1f | -22.13964 | -48.11758 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e65c6154-92da-32c6-9dee-c778e271edec | -22.13569 | -48.11701 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23774178-5e0e-35d7-bddf-fdda0e6cd84c | -22.1278 | -48.11589 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d2720da-0610-34f5-bb72-8b297f8223f8 | -22.12655 | -48.09432 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb23ec5-fdf3-309a-abc8-0e6e77e6d052 | -21.67685 | -47.71622 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dda95b6-d587-3028-acea-12c0d562113b | -21.67616 | -47.7218 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a91e16ff-d820-396b-94e1-ec2e2fb34283 | -21.67594 | -47.7141 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68dbeede-11d0-3e9c-a7fa-468b90993c21 | -21.67549 | -47.72733 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d4bbc4fc-e2e1-3532-8e8b-255940b8225d | -21.67521 | -47.71968 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3d1ceef-3832-3b0a-9708-f327d89a60c8 | -21.6748 | -47.73289 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README155.md)
